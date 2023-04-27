#!/bin/bash

# Use curl to send a request to the URL and get the size of the response body in bytes
size=$(curl -sI "$url" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r\n')

