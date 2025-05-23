#!/usr/bin/python3

password = "Password"

vowels = ['a', 'e', 'i', 'o', 'u']

print(f"{password} [Before]")

for i in password:
    if i.lower() in vowels:
        print("*", end="")
    else:
        print(i, end="")

print(" [After]")
