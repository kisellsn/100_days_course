import random
import turtle as turtle_module
from turtle import Turtle, Screen
colors = ["red", "green", "blue", "black", "pink", "orange", "yellow"]


screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_guess = screen.textinput("Make your bet", "Which turtle will win the race? Enter the color: ")


num_turtles = 6
turtles = []
for i in range(num_turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=140 - 50 * i)
    turtles.append(new_turtle)

def move_forward(turtle):
    turtle.forward(random.randint(0,10))


if user_guess: is_race_on = True
def race():
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winner = turtle
                return winner

            move_forward(turtle)

winner = race()
if winner.pencolor() == user_guess:
    print("Congratulations!")
else:
    print(f"Sorry. The winner is {winner.pencolor()}")

screen.exitonclick()