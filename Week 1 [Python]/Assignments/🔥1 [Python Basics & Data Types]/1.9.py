#!/usr/bin/python3

str = "H4ck3r"

print(f"Original  Word => {str}")
print("Converted Word => ", end="")

for i in str:
    if(i.islower()):
        print(chr(ord(i) - 32), end="")
    elif(i.isupper()):
        print(chr(ord(i) + 32), end="")
    else:
        print(i, end="")

print("") # Make New Line After Print The Word "H4ck3r"
