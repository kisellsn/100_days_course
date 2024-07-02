import turtle

import pandas
from turtle import Turtle, Screen
import turtle

ukraine_regions_data = pandas.read_csv("regions_ukr.csv")

print(ukraine_regions_data)


screen = Screen()
screen.title("Ukraine Regions Game")

img = "Ukraine_map.gif"
screen.addshape(img)

turtle.shape(img)

timm = Turtle()
timm.penup()
timm.hideturtle()
timm.speed(0)

# def get_mouse_click_coor(x, y):
#     print (f"{int(x)},{int(y)}")
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

user_guesses = []

while len(user_guesses) < len(ukraine_regions_data):
    user_answer = (screen.textinput(
        title=f"Guess a region {len(user_guesses)}/{len(ukraine_regions_data)}",
        prompt="What`s another region name?"
    ).title())

    if user_answer == "Exit":
        break

    if user_answer in ukraine_regions_data["region"].values:
        user_guesses.append(user_answer)

        x = ukraine_regions_data.loc[ukraine_regions_data["region"] == user_answer, "x"].values[0]
        y = ukraine_regions_data.loc[ukraine_regions_data["region"] == user_answer, "y"].values[0]

        timm.goto(x, y)
        timm.write(user_answer, align="center", font=("Arial", 14, "normal"))



screen.exitonclick()