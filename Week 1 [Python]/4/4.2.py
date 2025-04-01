#!/usr/bin/python3

def checkPassword(password):
    haveNum = False
    haveSpecialChar = False
    atLeast8Chars = (len(password) > 7)

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
               ":", ";", "<", "=", ">", "?", "@", "[", "]", "\\", "^", "_", "{", "}", "|"]

    for i in password:
        if i in special:
            haveSpecialChar = True
            continue

        if ord(i) - ord('0') in nums:
            haveNum = True

    return "Strong Password" if haveNum and haveSpecialChar and atLeast8Chars else "Week Password"


password = input("Enter Your Password : ")

print(f'Your Password "{password}" is {checkPassword(password)}')
