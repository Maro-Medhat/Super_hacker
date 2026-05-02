#!/usr/bin/python3

for i in range(1, 101):
    flag = True
    for j in range(2, i // 2 + 1): # range(2, int(i ** 0.5) + 1) is more efficient [Loop To Square Root Of i]
        if i % j == 0:
            flag = False
            break
    if flag and i != 1:
        print(i)
