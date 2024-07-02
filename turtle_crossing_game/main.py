import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.onkey(key="w", fun=player.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()

    if player.if_all_finish_line():
        player.reset()
        scoreboard.level_up()
        car_manager.speed_up()

    car_manager.move_cars()

    for car in car_manager.get_all_cars():
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break






screen.exitonclick()