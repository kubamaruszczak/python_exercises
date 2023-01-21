from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("snow")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # Movement speed
        self.x_speed = 10
        self.y_speed = 10

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.setposition(new_x, new_y)

    def wall_bounce(self):
        self.x_speed *= -1

    def ceiling_bounce(self):
        self.y_speed *= -1

    def player_bounce(self, segment_idx):
        if segment_idx == 0:
            self.y_speed *= -1
            if self.x_speed > 0:
                self.x_speed *= -1
        elif segment_idx == 1:
            self.y_speed *= -1
        else:
            self.y_speed *= -1
            if self.x_speed < 0:
                self.x_speed *= -1
