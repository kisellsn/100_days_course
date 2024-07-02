from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "right"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(50, 260)

        self.l_score = 0
        self.r_score = 0

        self.rewrite_scoreboard()

    def add_point(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.rewrite_scoreboard()

    def rewrite_scoreboard(self):
        self.write(f"{self.l_score}    {self.r_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)
