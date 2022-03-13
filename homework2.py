"""
Project: Homework2.5
Author: 염동환
Date of last update: March 13, 2022
Update list:
    -v1.0: March 13, 2022
"""
a_b=list(map(int,input("input a and b : ").split()))
a=a_b[0]
b=a_b[1]

print("a({:3d}) + b({:3d}) = {}".format(a,b,a+b))
print("a({:3d}) - b({:3d}) = {}".format(a,b,a-b))
print("a({:3d}) * b({:3d}) = {}".format(a,b,a*b))
print("a({:3d}) / b({:3d}) = {:.6f}".format(a,b,a/b))
print("a({:3d}) // b({:3d}) = {:.6f}".format(a,b,a//b))
print("a({:3d}) % b({:3d}) = {:.6f}".format(a,b,a%b))