#!/usr/bin/python3

import os

path = input("Enter Image Path : ")
os.system(f'exiftool "{path}"')
