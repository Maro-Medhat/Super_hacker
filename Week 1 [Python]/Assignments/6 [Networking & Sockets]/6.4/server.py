#!/usr/bin/python3

from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("Server is listening on port 12345...")

conn, addr = server_socket.accept()

print(f"Connection from {addr}")

data = conn.recv(1024).decode()
print(f"Client says: {data}")

conn.send("Hello from server!".encode())

conn.close()
