#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ "__main__":
    if (sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = "htpp://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})
    try:
        response_json = response.json()
        if response_json:
            print("[{}] {}".format(response_json['id'],
                                   response_json["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid Json)
