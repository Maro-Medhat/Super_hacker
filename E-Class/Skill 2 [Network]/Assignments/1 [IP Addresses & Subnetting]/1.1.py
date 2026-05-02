#!/usr/bin/pyton3

def isIPv4(ip): 
    octets = ip.split('.')

    if len(octets) != 4:
        return False

    for i in octets:
        i = int(i)
        if i < 0 or i > 255:
            return False
    
    return True
    
def isIPv6(ip):
    octets = ip.split(':')

    pool = "01213456789abcdefABCDEF"

    if len(octets) > 8:
        return False
    
    for i in octets:
        for j in i:
            if j not in pool:
                return False
            
    return True

ip = input("Enter Your IP : ")

if isIPv4(ip):
    print(f"[+] {ip} IPv4")

elif isIPv6(ip):
    print(f"[+] {ip} IPv6")

else:
    print("Invalid IP")
