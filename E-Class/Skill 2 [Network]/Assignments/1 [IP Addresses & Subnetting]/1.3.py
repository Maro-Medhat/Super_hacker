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

valid_ips = []

test = open("files/sample.txt", 'r')

temp = ""
pool = "0123456789."

for i in test.read():
    if i in pool:
        temp += i
    
    else:
        if isIPv4(temp):
            valid_ips.append(temp)
        temp = ""

print(valid_ips)

'''
cat files/sample.txt 
Here are some IP addresses:
- Valid: 192.168.1.1
- Also Valid: 8.8.8.8
- Internal IP: 10.0.0.1

Some garbage: 999.999.999.999,
not-an-ip, 172.16.300.1
Text continues here without IPs.
And another IP: 127.0.0.1
'''