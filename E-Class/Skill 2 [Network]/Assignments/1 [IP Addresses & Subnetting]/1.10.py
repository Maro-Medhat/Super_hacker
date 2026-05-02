#!/usr/bin/python3

import ipaddress

def isIPv4(ip):
  try:
    ip_obj = ipaddress.ip_address(ip)
    return ip_obj.version == 4
  except ValueError:
    return False

def calcNetworkAddress(ip, mask):
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')
    network_address = []

    for i in range(len(ip_octets)):
        network_address.append(str(int(ip_octets[i]) & int(mask_octets[i])))

    return ".".join(network_address)

ip1 = input("Enter IP1 : ")
mask1 = input("Enter Subnet Mask (IP1) : ")

ip2 = input("Enter IP2 : ")
mask2 = input("Enter Subnet Mask (IP2) : ")

try:
    if mask1 == mask2:
        network_address1 = calcNetworkAddress(ip1, mask1)
        network_address2 = calcNetworkAddress(ip2, mask2)
        if network_address1 == network_address2:
           print("Both IPs In The Same Subnet")
        else:
           print("Both IPs Are NOT In The Same Subnet")
    else:
        print("Both IPs Are NOT In The Same Subnet")

except:
   print("Syntax Erro, Try IPv4 Only")