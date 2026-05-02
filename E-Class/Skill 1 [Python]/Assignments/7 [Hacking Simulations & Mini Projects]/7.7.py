#!/usr/bin/python3

name = input("Enter Your Fake Name : ")
target = input("Enter Your Target Name : ")

message = f"""
Dear {target},

Your account has encountered an issue. Please verify your credentials here:
http://fake-login-page.com

Regards,
{name}
"""

print(message)

