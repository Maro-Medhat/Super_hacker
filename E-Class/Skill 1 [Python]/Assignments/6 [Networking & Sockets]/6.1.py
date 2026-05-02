#!/usr/bin/python3
'''
==========================
|| pip install requests ||
==========================
'''
import requests

res = requests.get("https://api.ipify.org?format=json")

if res.status_code == 200:
    print(f"Your Public IP Is : {res.json()['ip']}")

else:
    print("Failed To Fetch IP Address!!")



