from turtle import Turtle
from random import choice

STARTING_X = -383
STARTING_Y = 285

colors = ["red", "green", "blue", "yellow", "orange", "magenta"]


class Tile(Turtle):

    def __init__(self, color, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.penup()
        self.color(color)
        self.goto((x_pos, y_pos))

    def delete(self):
        self.goto((500, -500))


class TileManager:

    def __init__(self):
        self.all_tiles = []

    def create_tiles(self, rows_num: int):
        cur_x = STARTING_X
        cur_y = STARTING_Y

        for _ in range(rows_num):
            if len(colors) > 0:
                color = choice(colors)
                colors.remove(color)
            else:
                color = "red"
            for _ in range(20):
                new_tile = Tile(color, cur_x, cur_y)
                self.all_tiles.append(new_tile)
                cur_x += 40

            # Update creation pos before next row
            cur_x = STARTING_X
            cur_y -= 20
