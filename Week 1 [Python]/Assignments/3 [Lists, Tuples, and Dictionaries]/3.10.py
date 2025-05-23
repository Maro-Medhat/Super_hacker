#!/usr/bin/python3

credentials = {"root": "root", "kali": "kali", "user": 123456}

print("You Hacked Users DataBase :) \nWhich One You Want To Show It's Password? : ")

num = 1

for key in credentials.keys():
    print(f"{num}) {key}")
    num += 1

user = input()

print(f"{user} : {credentials[user]}")



