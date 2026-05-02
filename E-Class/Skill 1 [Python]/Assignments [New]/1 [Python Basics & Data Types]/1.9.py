#!/usr/bin/python3

str = "H4ck3r"
result = ""

for c in str:
    if c.islower():
        result += c.upper()
    elif c.isupper():
        result += c.lower()
    else:
        result += c    

print(f"Original  Word => {str}")
print(f"Converted Word => {result}")