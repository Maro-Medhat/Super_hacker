#!/usr/bin/python3

def rem_duplicate(arr):
    temp_arr = []
    for i in arr:
        if i not in temp_arr:
            temp_arr.append(i)
    return temp_arr

myArr = ["abc", 123, "Maro", 123, "abc"]

print(f"Before : {myArr}")

myArr = rem_duplicate(myArr)

print(f"After  : {myArr}")
