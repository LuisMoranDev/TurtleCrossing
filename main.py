
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 300

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
count = 0
car_list =[]

screen.onkey(player.move, "w")
screen.listen()
speed = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if count == 0 or count % 6 == 0:
        car = CarManager()
        car_list.append(car)
    for car in car_list:
        car.faster(speed)
        car.move()

        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= FINISH_LINE_Y:
        player.restart()
        speed += 1
        scoreboard.increase_score()

    count += 1


screen.exitonclick()