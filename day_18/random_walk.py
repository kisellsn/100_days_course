import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

timmy = Turtle()
timmy.shape("turtle")

timmy.width(6)
timmy.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
for _ in range(100):
    timmy.setheading((random.choice(directions)))
    timmy.color(random_color())
    timmy.forward(45)











screen = Screen()
screen.exitonclick()