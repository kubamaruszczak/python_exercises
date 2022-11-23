from turtle import Turtle

MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.setposition(new_x, new_y)

    def wall_bounce(self):
        self.y_speed *= -1

    def paddle_bounce(self):
        self.x_speed *= -1
        self.move_speed *= 0.99

    def restart(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED
        self.x_speed *= -1
