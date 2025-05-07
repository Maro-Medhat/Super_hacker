#!/usr/bin/python3

def checkPassword(password):
    haveNum = False
    haveSpecialChar = False
    atLeast8Chars = (len(password) > 7)

    nums = "0123456789"
    special = "!'#$%&()*+,-./:;<=>?@[]\\^_{}|"

    for i in password:
        if i in special:
            haveSpecialChar = True
        if i in nums:
            haveNum = True

    return "STRONG :)" if haveNum and haveSpecialChar and atLeast8Chars else "WEAK :("

password = input("Enter Your Password: ")
print(f'"{password}" -> {checkPassword(password)}')

