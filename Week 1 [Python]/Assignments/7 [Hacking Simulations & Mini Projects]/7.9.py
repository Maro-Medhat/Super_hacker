#!/usr/bin/python3

import random

def convert(num):
    n = int(num)
    result = n * 2
    return result if result < 10 else result - 9

cred = "4"
for _ in range(14):
    cred += str(random.randint(0, 9))

# Luhn Algorithm
sum = 0

for i in range(len(cred)):
    if i % 2 == 0:
        sum += convert(cred[i])
    else:
        sum += int(cred[i])

check_digit = 10 - sum % 10

cred += str(check_digit)

print("[Visa] : ", cred)

