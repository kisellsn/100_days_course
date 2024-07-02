from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "right"

with open("high_score.txt", "r") as file:
    HIGH_SCORE = int(file.read().split()[-1])


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(340, 260)

        self.high_score = HIGH_SCORE
        self.rewrite_scoreboard()

    def add_point(self):
        self.score += 1
        self.rewrite_scoreboard()

    def rewrite_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}. High score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.set_high_score(self.score)
        self.score = 0

        self.rewrite_scoreboard()

    def set_high_score(self, score):
        with open("high_score.txt", "w") as file:
            file.write(f"HIGH_SCORE = {score}")
        self.high_score = score
