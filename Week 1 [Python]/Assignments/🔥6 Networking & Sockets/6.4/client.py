#!/usr/bin/python3

from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("localhost", 12345))

client_socket.send("Hello from client!".encode())

data = client_socket.recv(1024).decode()
print(f"Server says: {data}")

client_socket.close()
