#!/usr/bin/python3

for i in range(1, 101):
    temp = ""

    if i % 3 == 0:
        temp += "Fizz"

    if i % 5 == 0:
        temp += "Buzz"

    if temp != "":
        print(temp)

    else:
        print(i, end=" ")
