#!/usr/bin/python3

"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
   response = requests.get("https://alx-intranet.hbtn.io/status")
   content = response.content.decode('utf-8')
   print("- type: {}".format(type(content)))
   print("- content: {}".format(content))
