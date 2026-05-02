#!/usr/bin/python3

def isIPv4(ip): 
    octets = ip.split('.')

    if len(octets) != 4:
        return False

    for i in octets:
        i = int(i)
        if i < 0 or i > 255:
            return False
    
    return True

ip = input("Enter Your IP (127.0.0.1/24) : ")

if isIPv4(ip.split('/')[0]):
    mask = int(ip.split('/')[1])
    print(f"Available IPs = {2 ** (32 - mask) - 2}")
else:
    print("Invalid IP!!")