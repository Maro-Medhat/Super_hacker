#!/usr/bin/python3

correct_password = "s3cr3t"
attempts = 0
while attempts < 3:
    password = input("Enter password : ")
    if password == correct_password:
        print("Login successful")
        break
    else:
        attempts += 1
        print(f"Wrong password. Attempts left: {3 - attempts}")
if attempts == 3:
    print("Account locked")