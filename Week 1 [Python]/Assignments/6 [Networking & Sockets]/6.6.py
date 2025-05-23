#!/usr/bin/python3

import requests

# Dictionary of fake headers to mimic Chrome browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

url = "https://httpbin.org/headers"

# Send the request with fake headers
response = requests.get(url, headers=headers)

# Print the server response
print("Server Response Headers:")
print(response.text)

