#!/usr/bin/python3

import requests

url = input("Enter URL : ")

r = requests.get(url)

print(f"[+] {url} is : UP" if r.status_code == 200 else f"[-] {url} is : Down")
