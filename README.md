# Syslog Receiver for Home Assistant

This is a custom integration for Home Assistant that receives Syslog messages over UDP and fires events.

## 🛠️ Installation

1. Add this repository as a [custom repository in HACS](https://hacs.xyz/)
2. Install the integration through HACS
3. Add to your `configuration.yaml`:

```yaml
syslog_receiver:
  port: 514
  allowed_ips: []       # Optional: List of allowed sender IPs
  keywords: []          # Optional: List of keywords to filter messages

When a message is received and passes filters, it fires the event syslog_message:
automation:
  - alias: Handle syslog
    trigger:
      platform: event
      event_type: syslog_message
    action:
      - service: notify.notify
        data:
          message: "Syslog: {{ trigger.event.data.message }}"
