#!/usr/bin/python3

def checkPassword(password):
    haveNum = False
    haveSpecialChar = False
    atLeast8Chars = len(password) > 7

    nums = "0123456789"
    special = "!'#$%&()*+,-./:;<=>?@[]\\^_{}|"

    for i in password:
        if i in special:
            haveSpecialChar = True
        elif i in nums:
            haveNum = True

    return "Strong Password" if haveNum and haveSpecialChar and atLeast8Chars else "Weak Password"

password = input("Enter Your Password : ")

print(f'Your Password "{password}" is {checkPassword(password)}')