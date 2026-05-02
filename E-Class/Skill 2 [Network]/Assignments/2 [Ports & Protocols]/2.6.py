#!/usr/bin/python3

def isPrivileged(port):
    return port in range(0, 1024)

port = int(input("Enter Your Port : "))

if isPrivileged(port):
    print(f"[+] {port} Privileged")
else :
    print(f"[-] {port} NOT Privileged")