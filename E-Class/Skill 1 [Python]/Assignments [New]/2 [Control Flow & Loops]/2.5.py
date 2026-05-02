#!/usr/bin/python3

def is_prime(n):
  if n == 1:
    return False
    
  elif n == 2:
    return True
    
  for j in range(2, int(n ** 0.5) + 1):
    if n % j == 0:
      return False
      
  return True

for i in range(1, 101):
  if is_prime(i):
    print(i)