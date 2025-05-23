#!/usr/bin/python3

str = input("Enter Any Word : ")

if str == str[::-1]:
    print(f'The Word "{str}" Is PALINDROME!!')
else:
    print(f'The Word "{str}" Is NOT PALINDROME!!')
