#!/usr/bin/python3

import os

print(os.listdir("files/delete_txt"))

q = input("Are You Sure You Want To Delete All Previous Files? [Y/N] : ")

if q == 'Y' or q == 'y':
    os.system("rm files/delete_txt/*")
    print("All Files Deleted Successfully!!")
