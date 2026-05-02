#!/usr/bin/python3

def get_ip_class(ip_address):
    try:
        first_octet = int(ip_address.split('.')[0])

        if 1 <= first_octet <= 126:
            return "Class A"
        elif first_octet == 127:
            return "Class A (Loopback Address)"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 254:
            return "Class E (Experimental)"
        else:
            return "Invalid IP Range"
    except:
        return "Invalid IP format"

ip = input("Enter An IP : ");

print("Your Ip Is : ", end="");
print(get_ip_class(ip));