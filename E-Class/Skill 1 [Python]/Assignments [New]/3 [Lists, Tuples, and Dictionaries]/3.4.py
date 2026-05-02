#!/usr/bin/python3

chars_map = {}

str = input("Enter Any Word : ")

for c in str:
    if c in chars_map.keys():
        chars_map[c] += 1
    else:
        chars_map[c] = 1

print(f'Analyisis Of Word "{str}" : ')

for key, value in chars_map.items():
    print(f"{key} -> {value}")