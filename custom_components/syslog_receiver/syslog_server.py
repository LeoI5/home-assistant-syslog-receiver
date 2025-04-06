import asyncio
import logging

_LOGGER = logging.getLogger(__name__)

class SyslogUDPServer:
    def __init__(self, hass, port=514, allowed_ips=None, keywords=None):
        self.hass = hass
        self.port = port
        self.allowed_ips = allowed_ips or []
        self.keywords = [k.lower() for k in keywords] if keywords else []
        self.transport = None

    async def start(self):
        loop = asyncio.get_running_loop()
        self.transport, _ = await loop.create_datagram_endpoint(
            lambda: SyslogProtocol(self.hass, self.allowed_ips, self.keywords),
            local_addr=("0.0.0.0", self.port)  # Просто слушаем на всех интерфейсах
        )
        _LOGGER.info(f"Syslog server started on 0.0.0.0:{self.port}")

    def stop(self):
        if self.transport:
            self.transport.close()
            _LOGGER.info("Syslog server stopped")

class SyslogProtocol:
    def __init__(self, hass, allowed_ips, keywords):
        self.hass = hass
        self.allowed_ips = allowed_ips
        self.keywords = keywords
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        _LOGGER.info("SyslogProtocol connection made")

    def datagram_received(self, data, addr):
        ip = addr[0]
        message = data.decode(errors='ignore').strip()
        _LOGGER.debug(f"Syslog from {ip}: {message}")

        # IP фильтр
        if self.allowed_ips and ip not in self.allowed_ips:
            _LOGGER.debug(f"Ignored syslog from {ip} (not in allowed_ips)")
            return

        message_lower = message.lower()

        # Если ключевые слова указаны — фильтруем
        if not self.keywords or any(keyword in message_lower for keyword in self.keywords):
            _LOGGER.info(f"Matched syslog from {ip}: {message}")
            self.hass.bus.fire("syslog_message", {
                "source_ip": ip,
                "message": message
            })
        else:
            _LOGGER.debug("No keyword match; message ignored")

    def connection_lost(self, exc):
        _LOGGER.info("SyslogProtocol connection lost")
