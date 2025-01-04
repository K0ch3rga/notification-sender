
from confluent_kafka import Consumer
import json

conf = {
    'bootstrap.servers': 'kafka:29092',  # Адрес Kafka-брокера
    'group.id': 'python-consumer-group',  # Идентификатор группы потребителей
    'auto.offset.reset': 'earliest'  # Начинать с самого раннего сообщения
}

consumer = Consumer(conf)

def consume_messages(topic):

    consumer.subscribe([topic])
    msg = consumer.poll(timeout=1.0)  # Ожидание сообщения с таймаутом

    if not msg is None and not msg.error():
        print(
            f'Received message: {msg.value().decode("utf-8")} from {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')
        return json.loads(msg.value().decode('utf-8'))


