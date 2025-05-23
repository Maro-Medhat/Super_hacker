#!/usr/bin/python3

msg = input("Enter Your Message : ")
num = int(input("Enter The Number You Want To XOR With : "))

enc_msg = ''.join(chr(ord(char) ^ num) for char in msg)

print(enc_msg)

'''
====================
||    Test Case   ||
====================
msg = "label"
num = 13
expected enc_msg = "aloha"
'''
