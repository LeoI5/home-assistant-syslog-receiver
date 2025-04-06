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
