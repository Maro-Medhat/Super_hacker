#!/usr/bin/python3

import os

def isIPv4(ip): 
    octets = ip.split('.')

    if len(octets) != 4:
        return False

    for i in octets:
        i = int(i)
        if i < 0 or i > 255:
            return False
    
    return True

ip = input("Enter Your IP : ")

if isIPv4(ip):
  os.system(f"ping -n 1 {ip}")
  
else:
  print("Invalid IP!!")