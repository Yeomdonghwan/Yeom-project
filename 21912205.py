import turtle
import math
from math import pi

base=float(input("밑변: "))
height=float(input("높이: "))

angle=math.atan(2*height/base)*180/pi
hypotenuse=((height**2)+((base/2)**2))**0.5

t=turtle.Turtle()
t.forward(base)
t.left(180-angle)
t.forward(hypotenuse)
t.left(2*angle)
t.forward(hypotenuse)


a=input()