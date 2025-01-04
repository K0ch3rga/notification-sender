#!/bin/sh

# kafka = "kafka:29092"
      
# blocks until kafka is reachable
echo -e "Available kafka topics: "
kafka-topics --bootstrap-server kafka:29092 --list

topics=(
  "email"
  "push_notifications"
  "telegram"
)


echo -e 'Creating kafka topics'
for topic in "${topics[@]}"; do
  echo "Creating topic: $topic"
  kafka-topics --bootstrap-server kafka:29092 --create --if-not-exists --topic "$topic" --replication-factor 1 --partitions 1
done

echo -e 'Successfully created the following topics:'
kafka-topics --bootstrap-server kafka:29092 --list
      