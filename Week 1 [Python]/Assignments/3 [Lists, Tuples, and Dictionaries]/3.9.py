#!/usr/bin/python3

def getLongestWord(arr):
    mx = 0
    temp = ""
    for i in arr:
        if len(i) > mx:
            mx = len(i)
            temp = i
    return temp

myArr = ["a", "ab", "abc", "Maroooooo"]

print(f"Original List {myArr}")

print(f'Longest Word is "{getLongestWord(myArr)}"')
