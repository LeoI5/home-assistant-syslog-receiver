
# 📡 Syslog Receiver for Home Assistant

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=flat-square)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/leoi5/home-assistant-syslog-receiver?style=flat-square)](https://github.com/leoi5/home-assistant-syslog-receiver/releases)
[![License](https://img.shields.io/github/license/leoi5/home-assistant-syslog-receiver?style=flat-square)](LICENSE)

**Syslog Receiver** is a Home Assistant integration that allows you to receive and filter **Syslog messages** over UDP, and trigger automations based on the received messages.

---

## 🔧 Features

- 📥 Receives Syslog messages over **UDP** (default port 514)
- 📝 Filters by **keywords** and **IP addresses**
- 🔔 Triggers Home Assistant events when messages are received
- 🧑‍💻 Easily configurable via **configuration.yaml**
- ✅ HACS support for easy installation

---

## 📥 Installation via HACS

1. Go to **HACS → Integrations → Custom repositories**
2. Add the repository:
   ```
   https://github.com/leoi5/home-assistant-syslog-receiver
   ```
   Type: **Integration**
3. Install the **Syslog Receiver** integration
4. Restart Home Assistant

---

## ⚙️ Configuration

Add the following configuration to your `configuration.yaml`:

```yaml
syslog_receiver:
  port: 514              # (Optional) Port to listen on. Default: 514
  allowed_ips:           # (Optional) Only allow messages from these IPs
    - 192.168.1.1
    - 10.0.0.2
  keywords:              # (Optional) Only accept messages containing these keywords
    - error
    - critical
```

Leave `allowed_ips` and `keywords` empty to accept all messages.

---

## 🛠️ Usage Example

You can create an automation to trigger on specific messages:

```yaml
automation:
  - alias: Notify on Syslog Error
    trigger:
      platform: event
      event_type: syslog_message
    condition:
      - condition: template
        value_template: >
          "error" in trigger.event.data.message | lower
    action:
      - service: notify.notify
        data:
          message: "Syslog Error: {{ trigger.event.data.message }}"
```

---

## 📡 Event Data

When a message is accepted, an event `syslog_message` is fired with the following data:

```json
{
  "event_type": "syslog_message",
  "data": {
    "ip": "192.168.1.1",
    "message": "<34>Apr 6 12:00:00 host app: error occurred"
  }
}
```

---

## 🧪 Testing

Run tests with:

```bash
pytest tests
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
