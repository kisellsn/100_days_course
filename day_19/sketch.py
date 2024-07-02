import random
import turtle as turtle_module
from turtle import Turtle, Screen
turtle_module.colormode(255)


tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_rigth():
    tim.right(10)
def turn_left():
    tim.left(10)

def clear():
    tim.home()
    tim.clear()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_rigth)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)


screen.exitonclick()