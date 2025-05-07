#!/usr/bin/python3

import os

ips = ["192.168.1.1", "8.8.8.8", "192.168.1.100"]

for ip in ips:
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

    if response == 0:
        print(f"[+] {ip} is online")

    else:
        print(f"[-] {ip} is offline")
