#!/usr/bin/python3

import random

secret = random.randint(1, 10)
guess = ""

while True:
    guess = int(input("Guess the number (1-10) : "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Your Guess Is Out Of Range")