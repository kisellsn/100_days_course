import random
import turtle
from turtle import Turtle

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

turtle.colormode(255)

def random_color():
    return (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random_color())
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() <= -300:
                car.hideturtle()
                self.cars.remove(car)
            else:
                car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT


    def get_all_cars(self):
        return self.cars


