#!/usr/bin/python3
# ================================
# ||         server.py          ||
# ================================
import socket

HOST = '127.0.0.1'   # Localhost
PORT = 5000          # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

data = conn.recv(1024).decode()
print(f"[+] Received message: {data}")

conn.close()
server_socket.close()