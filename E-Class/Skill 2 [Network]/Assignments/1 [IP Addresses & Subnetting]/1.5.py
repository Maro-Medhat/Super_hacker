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

def calcNetworkAddress(ip, mask):
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')
    network_address = []

    for i in range(len(ip_octets)):
        network_address.append(str(int(ip_octets[i]) & int(mask_octets[i])))

    return ".".join(network_address)

def calcBroadCastAddress(ip, mask):
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')
    not_mask_octets = []
    brodcast_address = []

    for i in mask_octets:
        not_mask_octets.append(255 - int(i))

    for i in range(len(ip_octets)):
        brodcast_address.append(str(int(ip_octets[i]) | int(not_mask_octets[i])))
    
    return ".".join(brodcast_address)
    

ip = input("Enter Your Ip : ")
mask = input("Enter Your Subnet Mask : ")

if isIPv4(ip):
    print(f"Network Address : {calcNetworkAddress(ip, mask)}")
    print(f"Brodcast Address : {calcBroadCastAddress(ip, mask)}")

else:
    print("Invalid IP!!")