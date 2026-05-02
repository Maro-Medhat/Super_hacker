#!/usr/bin/python3

# ================================
# ||         client.py          ||
# ================================

import socket

HOST = '127.0.0.1'   # Server IP
PORT = 5000          # Server Port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Hello from client!"
client_socket.send(message.encode())

client_socket.close()