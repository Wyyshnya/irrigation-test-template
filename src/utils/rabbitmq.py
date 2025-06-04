import pika
import json
from typing import Any

class RabbitMQClient:
    def __init__(self, host: str = "rabbitmq", queue: str = "irrigation_tasks"):
        self.host = host
        self.queue = queue
        self.connection = None
        self.channel = None

    def connect(self) -> None:
        """Устанавливает соединение с RabbitMQ."""
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue, durable=True)

    def send_message(self, message: Any) -> None:
        """Отправляет сообщение в очередь."""
        if not self.channel:
            self.connect()
        
        # Преобразуем сообщение в JSON, если оно не строка
        if not isinstance(message, str):
            message = json.dumps(message)
        
        self.channel.basic_publish(
            exchange="",
            routing_key=self.queue,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)  # Сообщения сохраняются
        )

    def close(self) -> None:
        """Закрывает соединение."""
        if self.connection and not self.connection.is_closed:
            self.connection.close()

    def __enter__(self):
        """Поддержка контекстного менеджера."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрытие соединения при выходе из контекста."""
        self.close()