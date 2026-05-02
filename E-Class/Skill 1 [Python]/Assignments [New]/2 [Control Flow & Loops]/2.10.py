#!/usr/bin/python3

s = input("Enter string : ")
if s == s[::-1]:
    print(f"{s} Is Palindrome")
else:
    print(f"{s} Is Not a palindrome")