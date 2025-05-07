#!/usr/bin/python3

import random
import string

char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

for i in range(12):
    print(char[random.randint(0, 91)], end="")

print("")

'''
chars = [
    # Capital letters (26 Chars)
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",

    # Small letters (26 Chars)
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",

    # Digits (10 Chars)
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",

    # Punctuation characters (30 Chars)
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}',

] #Total = 92 Char
'''
