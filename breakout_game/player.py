from turtle import Turtle

STARTING_POS = [(-20, -250), (0, -250), (20, -250)]


class Player:

    def __init__(self):
        self.segments = []
        self.create_player()

    def create_player(self):
        for pos in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("gainsboro")
            new_segment.shapesize(stretch_wid=0.5, stretch_len=1)
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move_left(self):
        if self.segments[0].xcor() > -390:
            for segment in self.segments:
                new_x = segment.xcor() - 10
                segment.setx(new_x)

    def move_right(self):
        if self.segments[-1].xcor() < 390:
            for segment in self.segments:
                new_x = segment.xcor() + 10
                segment.setx(new_x)

