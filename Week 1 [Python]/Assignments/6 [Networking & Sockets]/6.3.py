#!/usr/bin/python3

'''
==============================
||   pip install requests   ||
==============================
'''

import requests

res = requests.get("http://example.com")

print("Response Headers:\n")

for header, value in res.headers.items():
    print(f"{header}: {value}")


