#!/usr/bin/python3

def isValidIP(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False

    for i in octets:
        if i != str(int(i)) or int(i) < 0 or int(i) > 255:
            return False

    return True



ip = input("Enter an IPv4 : ")

status = "Valid" if isValidIP(ip) else "NOT Valid"

print(f"{ip} : {status}")
