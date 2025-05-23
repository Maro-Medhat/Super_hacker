#!/usr/bin/python3

import os

print("Files Are Here : files/convert_txt")

files = os.listdir("files/convert_txt")
converted_files = 0

for i in files:
    if i.endswith(".txt"):
        os.system(f"mv files/convert_txt/{i} files/convert_txt/{i[:-4]}.bak")
        converted_files += 1

print(f"{converted_files} files converted")

