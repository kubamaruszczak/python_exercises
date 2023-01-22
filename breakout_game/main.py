from turtle import Screen
from player import Player
from ball import Ball
from tile_manager import TileManager
from scoreboard import Scoreboard
from time import sleep


def start_game():
    global game_is_on
    game_is_on = True


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

# Ball creation
ball = Ball()

# Tile manager creation
tile_manager = TileManager()
tile_manager.create_tiles(1)

# Scoreboard creation
scoreboard = Scoreboard()

# Space callback
screen.onkey(start_game, "space")

game_is_on = False
while not game_is_on:
    # Wait for the space press to start the game
    screen.update()

# Register player movement callbacks
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

while game_is_on:
    sleep(0.1)
    ball.move()

    # Detect collision with the wall - SIDE WALL BOUNCE
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.wall_bounce()

    # Detect collision with the ceiling - TOP WALL BOUNCE
    if ball.ycor() > 250:
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

    # Detect collision with tile
    for tile in tile_manager.all_tiles:
        if tile.distance(ball) <= 20:
            if abs(tile.xcor() - ball.xcor()) < 15:
                ball.ceiling_bounce()
            else:
                ball.wall_bounce()

            scoreboard.add_point()
            tile_manager.delete_tile(tile)
            break

    # Detect end of the game
    if ball.ycor() < -280 or len(tile_manager.all_tiles) == 0:
        scoreboard.game_over()
        game_is_on = False

    screen.update()

screen.exitonclick()
