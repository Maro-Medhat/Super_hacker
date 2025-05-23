#!/usr/bin/python3

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

inp = input("Enter Your Text : ")

choose = input("1) Encrypt\n2) Decrypt\n")

shift = input("Shift By : ")


match choose:
    case "1":
        print(caesar_encrypt(inp, int(shift)))
    case "2":
        print(caesar_decrypt(inp, int(shift)))

