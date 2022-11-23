from turtle import Screen
from player import Player
from car_manager import CarsManager
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move, key="Up")

car_manager = CarsManager(25)
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    sleep(0.05)
    car_manager.gen_traffic()

    # Detect collision player with the car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when player cross the street
    if player.ycor() > 260:
        scoreboard.level_up()
        car_manager.speed_up()
        player.restart()

    screen.update()

screen.exitonclick()
