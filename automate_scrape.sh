#!/bin/bash

# Replace 3600 with the number of seconds you want between each run
INTERVAL=60

while true
do
    curl --header "Content-Type: application/json" \
      --request POST \
      --data '{"url": "http://phaidra.ai"}' \
      http://127.0.0.1:8080/

    sleep $INTERVAL
done
