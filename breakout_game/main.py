from turtle import Screen
from player import Player
from ball import Ball
from time import sleep

# Screen set up
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Player creation
player = Player()
# Registration of callbacks to move player sides
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Ball creation
ball = Ball()

game_is_on = True
while game_is_on:
    sleep(0.1)
    ball.move()

    # Detect collision with the wall - SIDE WALL BOUNCE
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.wall_bounce()

    # Detect collision with the ceiling - TOP WALL BOUNCE
    if ball.ycor() > 285:
        ball.ceiling_bounce()

    # Detect collision with the player
    # If ball passed player level
    if -250 < ball.ycor() < -230 and \
            (ball.xcor() < player.segments[-1].xcor() or ball.xcor() > player.segments[0].xcor()):
        # Find segment closes to the ball
        closest_segment_idx = 0
        smallest_distance = 1000
        for idx, segment in enumerate(player.segments):
            segment_ball_distance = abs(segment.xcor() - ball.xcor())
            if segment_ball_distance < smallest_distance:
                smallest_distance = segment_ball_distance
                closest_segment_idx = idx

        # Generate bounce depending on which segment was the closest one
        if ball.distance(player.segments[closest_segment_idx]) < 20:
            ball.player_bounce(closest_segment_idx)

    screen.update()

screen.exitonclick()
