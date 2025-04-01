#!/usr/bin/python3

import random

def genMACAdd():
    chars = "0123456789ABCDEF"
    mac = ["", "", "", "", "", ""]

    for i in range(6):
        for j in range(2):
            mac[i] = mac[i] + random.choice(chars)
    print(":".join(mac))


genMACAdd()

'''
==========================
=      Python Trcik      =
==========================

chars = "0123456789ABCDEF"
mac = [f"{random.choice(chars)}{random.choice(chars)}" for _ in range(6)]
'''
