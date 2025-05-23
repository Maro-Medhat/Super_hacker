#!/usr/bin/python3

def extract_vowels(msg):
    vowels = "aeiou"
    extracted_vowels = ''.join([char for char in msg if char in vowels])
    return extracted_vowels

msg = input("Enter Your Message : ")

print(f"Extracted vowels : {extract_vowels(msg)}")
