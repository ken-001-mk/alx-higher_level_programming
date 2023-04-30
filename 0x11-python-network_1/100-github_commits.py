#!/usr/bin/python3

"""Python script that takes 2 arguments in order
to solve a github commit challenge.
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                      .format(sys.argv[2], sys.argv[1]))
    n = r.json()
    try:
        for i in range(10):
            print(n[i].get('sha'), n[i].get('commit')
                  .get('author').get('name'), sep=": ")
    except IndexError:
        pass
