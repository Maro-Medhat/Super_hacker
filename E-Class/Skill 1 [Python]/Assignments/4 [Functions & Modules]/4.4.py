#!/usr/bin/python3

import hashlib

word = input("Enter A Word To Hash It With md5 : ")

encrypted_word = hashlib.md5(word.encode())

print(f"{encrypted_word.hexdigest()}")
