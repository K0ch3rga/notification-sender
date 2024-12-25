#!/bin/bash

# Wait for Kafka to be ready
until kafka-topics.sh --bootstrap-server localhost:9092 --list > /dev/null; do
  echo "Waiting for Kafka..."
  sleep 5
done

echo "Creating Kafka topics..."

# Create topics
topics=(
  "email"
  "push"
  "telegram"
)

for topic in "${topics[@]}"; do
  echo "Creating topic: $topic"
  kafka-topics.sh --create --if-not-exists --bootstrap-server localhost:9092 \
    --replication-factor 1 --partitions 1 --topic "$topic"
done

echo "Topics created successfully:"
kafka-topics.sh --bootstrap-server localhost:9092 --list