from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.setheading(180)
        self.speed = 0

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.speed)

    def faster(self, num):
        self.speed = MOVE_INCREMENT * num



