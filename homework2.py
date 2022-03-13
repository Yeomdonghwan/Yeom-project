"""
Project: Homework2.4
Author: 염동환
Date of last update: March 13, 2022
Update list:
    -v1.0: March 13, 2022
"""
print("===============================")
print("Decimal  Bit   Octal Hexadecimal")
print("-------------------------------")
for i in range(0,256):
    print("{0:6d} {1:08b} {2:#05o} {3:#04X}".format(i,i,i,i))