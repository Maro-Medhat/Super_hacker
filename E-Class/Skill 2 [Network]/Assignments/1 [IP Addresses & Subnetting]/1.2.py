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

ip = input("Enter Your IP : ")

if isIPv4(ip):
    octets = ip.split('.')
    new_octets = []
    for i in octets:
        new_octets.append(f"{int(i):08b}")
    print(".".join(new_octets))

else:
    print("Invalid IP!!")