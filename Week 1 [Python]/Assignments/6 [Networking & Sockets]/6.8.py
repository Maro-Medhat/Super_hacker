#!/usr/bin/python3

import os

print("Note : This Code Will Take 4:25 Minute To Finish ;-;")

for i in range(1, 255):
    ip = f"192.168.1.{i}"
    response = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"[+] {ip} is online")

