import {Kafka} from "kafkajs";
import {kafkaConfig} from "../config";
import {TelegramService} from "./telegram.service";
import {MessageDTO} from "../../core/dtos/MessageDTO";
import {logger} from './logger';

const kafka = new Kafka({clientId: kafkaConfig.clientId, brokers: kafkaConfig.brokers});
const consumer = kafka.consumer({groupId: kafkaConfig.groupId});

export const startKafkaConsumer = async (telegram: TelegramService) => {
    try {
        await consumer.connect();
        console.log("Connected to Kafka");

        await consumer.subscribe({topic: kafkaConfig.topic, fromBeginning: false});
        console.log("Subscribing to Kafka");

        await consumer.run({
            eachMessage: async ({ message }) => {
                try {
                    logger.info(`Сообщение из Kafka получено ${JSON.stringify(JSON.parse(message.value?.toString() ?? ''))}`);
                    const {type, address, title, message: text} = JSON.parse(JSON.stringify(JSON.parse(message.value?.toString() ?? '')));
                    const messageDTO = new MessageDTO(type, address, title, text);

                    console.log(`Получено сообщение из Kafka: type: ${messageDTO.type}, address: ${messageDTO.address}, title: ${messageDTO.title}, message: ${messageDTO.message}`);

                    if (messageDTO.type === 'telegram') {
                        telegram.sendMessage(messageDTO)
                    }
                } catch (error) {
                    console.error('Ошибка при обработке сообщения из Kafka:', error);
                }
            }
        });
    } catch (error) {
        console.error('Ошибка при подключении Kafka Consumer:', error);
    }
}
