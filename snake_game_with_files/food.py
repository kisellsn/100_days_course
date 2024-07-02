import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")

        self.change_location()

    def change_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
