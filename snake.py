from turtle import Turtle

EAST, NORTH, WEST, SOUTH = 0, 90, 180, 270


class Snake:
    def __init__(self):
        self.body = []
        self.initialize()
        self.head = self.body[0]
        self.heading = 0
        self.segments_pos = [segment.position() for segment in self.body]

    def initialize(self):
        for step in range(5):
            segment = Turtle(shape="square")
            segment.speed(0)
            segment.penup()
            segment.setx(-20 * step)
            segment.color("#69db7c")
            self.body.append(segment)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            x, y = self.body[segment - 1].position()
            self.body[segment].goto(x, y)

        self.body[0].setheading(self.heading)
        self.body[0].forward(20)

    def grow(self):
        segment = Turtle(shape="square")
        segment.speed(0)
        segment.penup()
        segment.color("#69db7c")
        x, y = self.body[-1].position()
        segment.setposition(x, y)
        self.body.append(segment)
        self.segments_pos = [(round(segment.xcor()), round(segment.ycor())) for segment in self.body]

    def head_north(self):
        if self.heading != SOUTH:
            self.heading = NORTH

    def head_south(self):
        if self.heading != NORTH:
            self.heading = SOUTH

    def head_west(self):
        if self.heading != EAST:
            self.heading = WEST

    def head_east(self):
        if self.heading != WEST:
            self.heading = EAST

    def hide_snake(self):
        for segment in self.body:
            segment.hideturtle()

    def show_snake(self):
        for segment in self.body:
            segment.showturtle()
