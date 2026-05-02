#!/usr/bin/python3

chars_map = {}

str = input("Enter Any Word : ")

for i in str:
    if i in chars_map.keys():
        chars_map[i] += 1
    else:
        chars_map[i] = 1

print(f'Analyisis Of Word "{str}" : ')

for key, value in chars_map.items():
    print(f"{key} -> {value}")
