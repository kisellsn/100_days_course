import random
import time
from turtle import Screen, Turtle

from pong_game.ball import Ball
from pong_game.scoreboard import Scoreboard
from pong_game.paddle import Paddle


screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pin Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball((0, 0))

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
paddle_direction = 1
while game_is_on:
    time.sleep(0.05)
    screen.update()
    # if r_paddle.ycor() < -250 or r_paddle.ycor() > 250:
    #     paddle_direction *= -1
    #
    # if paddle_direction > 0:
    #     r_paddle.up()
    # else:
    #     r_paddle.down()


    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_y()
    # elif ball.xcor() < -390 or ball.xcor() > 390:
    #     game_is_on = False
    elif ((ball.distance(r_paddle) < 50 and ball.xcor() > 320)
            or (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
        ball.change_direction_x()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_point("r")
        ball.increase_speed()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_point("l")
        ball.increase_speed()
    scoreboard.rewrite_scoreboard()













screen.exitonclick()