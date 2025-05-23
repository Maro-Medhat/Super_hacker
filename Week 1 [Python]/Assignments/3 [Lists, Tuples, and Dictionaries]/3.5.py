#!/usr/bin/python3

arr = [5, 4, 2, 1, 7, 3, 6]

print(f"Before : {arr}")

# Using Manual [Bubble Sort]
for i in range(len(arr)):
    temp = 0
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]: # Swap arr[j] & arr[j + 1]
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(f"After  : {arr}")
