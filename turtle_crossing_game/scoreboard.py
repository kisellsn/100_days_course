from turtle import TurtleScreen, Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0

        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.rewrite()

    def level_up(self):
        self.level += 1
        self.clear()

        self.rewrite()

    def rewrite(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

