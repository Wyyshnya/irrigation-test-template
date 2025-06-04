# Работа с RabbitMQ

Этот модуль предоставляет функциональность для отправки сообщений в RabbitMQ, используемый в проекте как брокер сообщений.

## Модуль: `rabbitmq.py`

### Описание
Класс `RabbitMQClient` позволяет:
- Подключаться к RabbitMQ.
- Отправлять сообщения в очередь.
- Управлять соединением через контекстный менеджер.

### Использование

#### Инициализация
```python
from src.utils.rabbitmq import RabbitMQClient

# Создание клиента с настройками по умолчанию (host="rabbitmq", queue="irrigation_tasks")
client = RabbitMQClient()