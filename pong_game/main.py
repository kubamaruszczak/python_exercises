from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()

scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    sleep(ball.move_speed)
    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with a paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.paddle_bounce()

    # Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.restart()

    # Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.restart()

    screen.update()

screen.exitonclick()
