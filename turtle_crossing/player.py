from turtle import Turtle

STARTING_POS = (0, -270)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move(self):
        self.sety(self.ycor() + 5)

    def restart(self):
        self.goto(STARTING_POS)
