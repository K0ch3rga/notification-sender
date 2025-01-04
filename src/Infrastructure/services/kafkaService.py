
from confluent_kafka import Consumer
import json

def consume_messages(topic):
    pass
    # conf = {
    #     'bootstrap.servers': 'kafka:29092',  # Адрес Kafka-брокера
    #     'group.id': 'python-consumer-group',    # Идентификатор группы потребителей
    #     'auto.offset.reset': 'earliest'         # Начинать с самого раннего сообщения
    # }
    #
    # consumer = Consumer(conf)
    # consumer.subscribe([topic])
    #
    # try:
    #     while True:
    #         msg = consumer.poll(timeout=1.0)  # Ожидание сообщения с таймаутом
    #
    #         if msg is None:
    #             continue
    #         if not msg.error():
    #             email_data = json.loads(msg.value().decode('utf-8'))
    #             print(
    #                 f'Received message: {msg.value().decode("utf-8")} from {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     # Закрытие потребителя
    #     consumer.close()
