from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#ff8787")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        random_x = randint(-14, 14) * 20
        random_y = randint(-14, 14) * 20
        self.goto(random_x, random_y)
