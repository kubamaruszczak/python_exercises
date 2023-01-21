from turtle import Screen
from player import Player
from time import sleep

# Screen set up
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Player creation and registration of callbacks to move player sides
player = Player()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

screen.exitonclick()
