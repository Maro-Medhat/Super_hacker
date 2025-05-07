#!/usr/bin/python3

from socket import *

target = "scanme.nmap.org"

print(f"Scanning {target} for open ports from 20 to 100...\n")

for port in range(20, 101):
    s = socket(AF_INET, SOCK_STREAM) # Create Socket
    s.settimeout(0.5) #  Make 0.5sec For Each Port Scan ... If No Response Will Ignore Current Port
    result = s.connect_ex((target, port)) # Try To Connect To Current Port


    if result == 0 :
        print(f"[+] Port {port} Open")




'''
=====================
||      Notes      ||
=====================
socket(AF_INET, SOCK_STREAM)
    socket.AF_INET -> [Using IPv4]
    socket.SOCK_STREAM -> [Using TCP]
'''
