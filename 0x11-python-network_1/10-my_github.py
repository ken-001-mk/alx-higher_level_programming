#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
