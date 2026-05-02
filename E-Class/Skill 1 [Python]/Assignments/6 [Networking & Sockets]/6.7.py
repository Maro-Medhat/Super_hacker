#!/usr/bin/python3

import requests

url = input("Enter a website url: ")

if not url.startswith(("http://", "https://")):
    url = "http://" + url

res = requests.get(url, timeout=5)

if res.status_code == 200:
    print(f"{url} is online")
else:
    print(f"{url} is down (Status code: {res.status_code})")
