#!/usr/bin/python3

port = int(input("Enter Your Port (1-65535) : "))

if port in range(1, 65536):
  print("[+] Valid Port!!")
else:
  print("[-] Invalid Port!!")