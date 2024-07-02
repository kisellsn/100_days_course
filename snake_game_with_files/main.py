import random
import time
from turtle import Screen

from snake_game_with_files.scoreboard import Scoreboard
from snake_game_with_files.snake import Snake
from snake_game_with_files.food import Food


screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_location()
        snake.add_snake_piece()

        scoreboard.add_point()

    if snake.head.xcor() < -400 or snake.head.xcor() > 400 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()
            break





screen.exitonclick()