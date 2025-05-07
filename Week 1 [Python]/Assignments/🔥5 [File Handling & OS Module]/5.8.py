#!/usr/bin/python3

import os
from zipfile import *

print("Files Are Here : files/compress_txt")

print(os.listdir("files/compress_txt"))

file_name = input("Choose File To Compress [Without .txt] : ")

zip_file = ZipFile(f"files/compress_txt/{file_name}.zip", "w")
zip_file.write(f"files/compress_txt/{file_name}.txt", arcname=f"{file_name}.txt")

zip_file.close()


print("1 File Compressed Successfully!!")

print(os.listdir("files/compress_txt"))
