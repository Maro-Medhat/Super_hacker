#!/usr/bin/python3

import random
import string

domains = ["example.com", "testmail.com", "fakeinbox.com"]
emails = []

for _ in range(10):
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(domains)
    print(f"{user}@{domain}")
