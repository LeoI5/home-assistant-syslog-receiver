
# 📡 Syslog Receiver for Home Assistant

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=flat-square)](https://hacs.xyz/)
[![Version](https://img.shields.io/github/v/release/leoi5/home-assistant-syslog-receiver?style=flat-square)](https://github.com/leoi5/home-assistant-syslog-receiver/releases)
[![License](https://img.shields.io/github/license/leoi5/home-assistant-syslog-receiver?style=flat-square)](LICENSE)

[English version](README_en.md)

**Syslog Receiver** интеграция для Home Assistant, которая позволяет получать и фильтровать **Syslog-сообщения** по UDP, а также запускать автоматизации на основе полученных сообщений.

---

## 🔧 Особенности

- 📥 Принимает Syslog-сообщения по **UDP** (по умолчанию порт 514)
- 📝 Поддержка фильтрации по **ключевым словам** и **IP-адресам**
- 🔔 Генерирует события Home Assistant при получении сообщений
- 🧑‍💻 Легко настроить через **configuration.yaml**
- ✅ Поддержка **HACS** для легкой установки

---

## 📥 Установка через HACS

1. Перейдите в **HACS → Integrations → Custom repositories**
2. Добавьте репозиторий:
   ```
   https://github.com/leoi5/home-assistant-syslog-receiver
   ```
   Тип: **Integration**
3. Установите интеграцию **Syslog Receiver**
4. Перезагрузите Home Assistant

---

## ⚙️ Настройка

Добавьте следующую конфигурацию в ваш `configuration.yaml`:

```yaml
syslog_receiver:
  port: 514              # (Опционально) Порт для прослушивания. По умолчанию: 514
  allowed_ips:           # (Опционально) Разрешённые IP-адреса
    - 192.168.1.1
    - 10.0.0.2
  keywords:              # (Опционально) Ключевые слова для фильтрации
    - error
    - critical
```

Оставьте `allowed_ips` и `keywords` пустыми, чтобы принимать все сообщения.

---

## 🛠️ Пример использования

Можно создать автоматизацию, которая будет срабатывать при получении сообщений:

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

## 📡 Данные события

Когда сообщение проходит фильтрацию, генерируется событие `syslog_message` с данными:

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

## 🧪 Тестирование

Запустите тесты:

```bash
pytest tests
```

---

## 📄 Лицензия

Этот проект лицензирован под MIT. Подробнее см. в [LICENSE](LICENSE).
