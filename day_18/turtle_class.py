import random
from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")

# pen_is_down = True
# for _ in range(15):
#     timmy.forward(10)
#     if pen_is_down:
#         timmy.penup()
#         pen_is_down = False
#     else:
#         timmy.pendown()
#         pen_is_down = True
timmy.width(6)
num_of_sides = [3, 4, 5, 6, 7]
colors = ["red", "green", "blue", "purple", "orange", "pink", "beige"]
for sides in num_of_sides:
    timmy.color(random.choice(colors))
    angle = 360 / sides
    for _ in range(sides):
        timmy.right(angle)
        timmy.forward(100)










screen = Screen()
screen.exitonclick()