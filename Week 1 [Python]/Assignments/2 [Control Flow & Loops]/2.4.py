#!/usr/bin/python3

year = int(input("Enter a Year : "))

str = "LEAP" if year % 4 == 0 else "NORMAL"

print(f"{year} Is {str} Year!!") 
