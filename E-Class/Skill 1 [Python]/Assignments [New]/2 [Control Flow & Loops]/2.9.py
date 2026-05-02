#!/usr/bin/python3

correct_password = "s3cr3t"
while True:
    password = input("Enter password : ")
    if password == correct_password:
        print("Correct!")
        break
    else:
        print("Wrong, try again")