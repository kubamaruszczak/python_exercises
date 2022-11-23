from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-210, 255)
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=("Courier", 25, "normal"), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=("Courier", 25, "normal"), align="center")