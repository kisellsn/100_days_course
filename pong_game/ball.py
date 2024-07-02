import random
from turtle import Turtle



class Ball(Turtle):
    speed = 10
    def __init__(self, pos):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(pos)
        self.setheading(random.randint(1, 360))

    def move(self):
        self.forward(self.speed)

    def change_direction_y(self):
        new_heading = (360 - self.heading()) % 360
        self.setheading(new_heading)

    def change_direction_x(self):
        new_heading = (180 - self.heading()) % 360
        self.setheading(new_heading)

    def reset(self):
        self.goto(0, 0)
        self.change_direction_x()

    def increase_speed(self):
        self.speed += 1
