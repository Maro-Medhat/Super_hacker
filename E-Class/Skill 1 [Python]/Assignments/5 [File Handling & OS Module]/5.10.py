#!/usr/bin/python3

import os


print("=" * 95)
print("||" + " " * 31 + "Welcome to the CTF challenge!" + " " * 31 + "||")
print("||" + " " * 13 + "There are 7 files available, each containing different messages." + " " * 14 + "||")
print("||" + " " * 12 + "Your goal is to search through these files to find the hidden flag." + " " * 12 + "||")
print("||" + " " * 4 + "Luckily, I've prepared a script that searches for a specific word inside each file." + " " * 4 + "||")
print("||" + " " * 30 + "Good luck in finding the FLAG!!" + " " * 30 + "||")
print("=" * 95, end="\n\n")

files = os.listdir("files/flag_txt")

word = input("Type Something To Search In This Files : ")

print()

for c in files:
    print(f"{c} : ")
    os.system(f"grep {word} files/flag_txt/{c}")
    print("\n------------------------------\n")
