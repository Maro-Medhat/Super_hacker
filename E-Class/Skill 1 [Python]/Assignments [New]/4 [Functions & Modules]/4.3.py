#!/usr/bin/python3

import random
import string

def generate_password():
  temp = ""
  pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'#$%&()*+,-./:;<=>?@[]\\^_{}|"
  for i in range(12):
    temp += (pool[random.randint(0, len(pool) - 1)])
  return temp

password = generate_password()

print(f"Here Is Your Password : {password}")