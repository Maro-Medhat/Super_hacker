#!/usr/bin/python3

while True:
    password = input("Enter The Password : ")
    if password == "s3cr3t":
        break
    else:
        print("Incorrect Password, Try Again!!")

print("Correct Password!!")
