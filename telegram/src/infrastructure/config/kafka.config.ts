export const kafkaConfig = {
    brokers: [process.env.KAFKA_BROKER || 'localhost:9092'],
    clientId: process.env.KAFKA_CLIENT_ID || 'notification-service',
    groupId: process.env.KAFKA_GROUP_ID || 'notification-group',
    topic: process.env.KAFKA_TOPIC || 'telegram',
};
