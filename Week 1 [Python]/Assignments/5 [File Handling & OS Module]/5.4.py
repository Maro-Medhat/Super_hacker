#!/usr/bin/python3

import os

print("Text Is Here : files/count_words.txt")

input_word = input("Search for ... : ")

print(f"\n{input_word} : ", end="")

command = f'grep -w -i -o "{input_word}" files/count_words.txt | wc -l'
os.system(command)

'''
Explain : command = f'grep -w -i -o "{input_word}" files/count_words.txt | wc -l'

[-w] Match whole word only
[-i] Case insensitive
[-o] Print each found in new line
---------------------------------
[wc] Stands for word count command
[-l] Count lines
'''
