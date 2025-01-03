#!/bin/bash

container_name="$1"
timeout=${2:-60}

if [ -z "$container_name" ]; then
    echo "No container name specified"
    exit 1
fi

echo "Checking health for container: $container_name"
try=0
is_healthy="false"

while [ "$is_healthy" != "true" ]; do
    try=$((try + 1))
    printf "■"
    is_healthy=$(docker inspect --format='{{json .State.Health.Status}}' "$container_name" | tr -d '"')
    sleep 1

    if [[ $try -eq $timeout ]]; then
        echo "Container did not boot within timeout"
        exit 1
    fi
done

echo "Container $container_name is healthy!"
