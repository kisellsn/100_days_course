import time
import turtle as turtle_module
from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

START_POSITION = (0, 0)


class Snake():
    head = None

    def __init__(self):
        self.body = []
        self.snake_size = 0

        self.create_snake()

        self.head = self.body[0]

    def create_snake(self):
        for _ in range(3):
            self.add_snake_piece(START_POSITION)

    def add_snake_piece(self, pos=None):

        new_piece = turtle_module.Turtle(shape="square")
        new_piece.penup()
        new_piece.color("white")

        pos = self.body[-1].position() if pos is None else pos
        new_piece.goto(pos)

        self.body.append(new_piece)
        self.snake_size += 1

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def reset(self):
        for piece in self.body:
            piece.goto(-1000, -1000)

        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
