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

def isPrivateIP(ip):
    octets = ip.split('.')

    # Private (A)
    if(octets[0] == "10"):
        return True
    # Private (B)
    elif (octets[0] == "172" and (int(octets[1]) >= 16 and int(octets[1]) <= 31)):
        return True
    # Private (C)
    elif (octets[0] == "192") and (octets[1] == "168"):
        return True
    # Link-Local
    elif (octets[0] == "192") and (octets[1] == "168"):
        return True
    # Loopback
    if(octets[0] == "127"):
        return True
    # CGNAT(ISPs)
    elif (octets[0] == "100" and (int(octets[1]) >= 64 and int(octets[1]) <= 127)):
        return True
    else:
        return False

ip = input("Enter Your IP : ")

if isIPv4(ip):
    if isPrivateIP(ip):
        print("Your Ip Is PRIVATE!!")
    else:
        print("Your IP Is NOT PRIVATE!!")
else:
    print("Invalid IP!!")