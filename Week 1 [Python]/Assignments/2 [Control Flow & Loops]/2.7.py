#!/usr/bin/python3

import random

flag = False
rand_num = random.randint(1, 5)
attemps = 3

print("Hello, Let's Play A Simple Guess Number Game!! :)", end="\n\n")
print("I Choosed A Number From [1 - 5]", end="\n\n")
print("If You Can Guess It Before 3 Attemps, YOU WIN!! ^-^", end ="\n\n")

while attemps > 0:
    num = int(input(f"{attemps}# Guess Number : "))
    if num == rand_num:
        flag = True
        break
    attemps -= 1
    print("")

print("\n=====================================\n")
print("YOU WIN!!") if flag else print(f"Sorry, YOU LOSE :( [My Number Was {rand_num}]")
print("\n=====================================\n")
