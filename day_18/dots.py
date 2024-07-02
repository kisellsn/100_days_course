import random
import turtle

import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)
# colors = colorgram.extract('img.png', 10)
# print(colors)
#
# new_colors = []
# for color in colors:
#     new_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

colors = [(108, 91, 71), (55, 41, 24), (84, 91, 118), (172, 161, 137), (148, 153, 169), (90, 98, 93), (228, 221, 199), (33, 38, 57), (117, 73, 86), (44, 48, 115)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
timmy.penup()
timmy.setpos(-250,-250)


def new_row():
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)


for row in range(10):
    for dot in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    new_row()





screen = Screen()
screen.exitonclick()