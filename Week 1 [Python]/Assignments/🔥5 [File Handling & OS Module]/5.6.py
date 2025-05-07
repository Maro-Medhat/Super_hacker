#!/usr/bin/python3

import os

print("=============================================")
print("||  Hey!, I will make a file for you ^-^   ||")
print("=============================================")
file_name = input("Enter File Name : ")

msg = input("Enter Something To Save In Your File : ")

os.system(f"echo {msg} > files/generate_txt/{file_name}.txt")

print(f"files/generate_txt/{file_name}.txt : {msg}")

