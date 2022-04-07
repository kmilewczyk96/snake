from turtle import Turtle
from random import choice


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#ff8787")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.spawn(blocked_pos=[])

    def spawn(self, blocked_pos: list):
        available = []
        blocked_pos.append((int(self.xcor()), int(self.ycor())))
        for x in range(-19, 20):
            x *= 20
            for y in range(-19, 20):
                y *= 20
                if (x, y) not in blocked_pos:
                    available.append((x, y))

        self.goto(choice(available))
