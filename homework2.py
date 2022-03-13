"""
Project: Homework2.1
Author: 염동환
Date of last update: March 13, 2022
Update list:
    - v1.0: March 13, 2022
"""
from math import pi
radius = int(input("radius = "))
area = pi*radius*radius
circumference = 2*pi*radius

print("Circle of radius ({}) : area ({}), circumference ({})" .format(radius,area,circumference))