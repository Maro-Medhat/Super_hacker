#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

while True:
    print(s.recvfrom(65565))
