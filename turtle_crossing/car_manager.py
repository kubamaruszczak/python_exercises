from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_X = 320

CAR_SPEED = 5
SPEED_INCREASE = 1


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(STARTING_X, random.randint(-220, 230))

    def move(self, speed):
        self.setx(self.xcor() - speed)


class CarsManager:
    def __init__(self, max_num):
        self.cars = []
        self.speed = CAR_SPEED
        self.max_num = max_num

    def add_car(self):
        if len(self.cars) < self.max_num:
            self.cars.append(Car())

    def relocate_car(self):
        for car in self.cars:
            if car.xcor() < random.randint(-450, -320):
                car.goto(STARTING_X, random.randint(-220, 230))

    def move_cars(self):
        for car in self.cars:
            car.move(self.speed)

    def gen_traffic(self):
        if random.choice([0, 0, 0, 0, 0, 0, 1]):
            self.add_car()
        self.move_cars()
        self.relocate_car()

    def speed_up(self):
        self.speed += SPEED_INCREASE

