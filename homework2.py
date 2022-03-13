"""
Project: Homework2.2
Author: 염동환
Date of last update: March 13, 2022
Update list:
    -v1.0: March 13, 2022
"""
width_length=list(map(int,input("width, length = ").split()))
width = width_length[0]
length = width_length[1]
area = width*length
perimeter = 2*width + 2*length
print("Rectangle of width({}) and length({}) : area ({}), perimeter({})".format(width,length,area,perimeter))