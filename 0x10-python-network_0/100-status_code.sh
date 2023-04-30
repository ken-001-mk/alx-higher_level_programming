#!/bin/bash

# script that sends a request to a URL passed as an argument
#displays only the status code of the response.
curl -o /dev/null --silent -Iw "%{http_code}" "$1"
