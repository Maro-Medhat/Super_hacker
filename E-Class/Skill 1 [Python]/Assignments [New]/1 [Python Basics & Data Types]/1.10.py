#!/usr/bin/python3

old_pass = "Password"
vowels = "aeiouAEIOU"
new_pass = ""

for c in old_pass:
    if c in vowels:
        new_pass += "*"
    else:
        new_pass += c

print(f"{old_pass} [Before]")
print(f"{new_pass} [After]")