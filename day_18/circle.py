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

def draw(size_of_gap):
    for angle in range(int(360 / size_of_gap)):
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.color(random_color())
        timmy.circle(100)

draw(12)









screen = Screen()
screen.exitonclick()