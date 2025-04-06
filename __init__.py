import asyncio
import logging

from .syslog_server import SyslogUDPServer
from homeassistant.const import EVENT_HOMEASSISTANT_STOP

_LOGGER = logging.getLogger(__name__)
DOMAIN = "syslog_receiver"

async def async_setup(hass, config):
    conf = config.get(DOMAIN, {})
    port = conf.get("port", 514)
    allowed_ips = conf.get("allowed_ips", [])
    keywords = conf.get("keywords", ["error"])

    server = SyslogUDPServer(hass, port=port, allowed_ips=allowed_ips, keywords=keywords)
    await server.start()

    async def shutdown(event):
        server.stop()

    hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STOP, shutdown)
    return True
