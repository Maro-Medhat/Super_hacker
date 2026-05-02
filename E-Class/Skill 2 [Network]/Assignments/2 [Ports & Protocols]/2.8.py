#!/usr/bin/python3

import socket

host = input("Enter host (ex. 127.0.0.1): ").strip()

# Scan ports 1–1024 (you can change this)
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] OPEN  {port}/tcp")
    finally:
        s.close()