#!/usr/bin/python3

import os

print("Files Are Here : files/large_txt")

files = os.listdir("files/large_txt")
print(files)

mx = 0
largest_file = ""

for f in files:
    if os.path.getsize(f"files/large_txt/{f}") > mx:
        mx = os.path.getsize(f"files/large_txt/{f}")
        largest_file = f

print("==============================================")
print(f"||        Largest file is : {largest_file}         ||")
print("==============================================")

'''
============================
||       Short Code       ||
============================

import os

files = os.listdir("files/large_txt")

files.sort(key=lambda f: os.path.getsize(f"files/large_txt/{f}"))

print(files[-1])
'''
