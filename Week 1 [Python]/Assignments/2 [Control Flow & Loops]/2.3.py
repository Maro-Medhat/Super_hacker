#!/usr/bin/python3

for i in range(10000):
    if i < 10:
        print(f"000{i}")
    elif i < 100:
        print(f"00{i}")
    elif i < 1000:
        print(f"0{i}")
    else:
        print(i)

# ==========================
# ||     Shorter Code     ||
# ==========================

# for i in range(10000):
#    print(f"{i:04}")
