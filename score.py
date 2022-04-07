import json
import os.path
from os import path
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__(shape="square", visible=False)
        self.score = 0
        self.color("black")
        self.penup()

        self.highscores = []
        self.get_highscores()

    def result(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(
            "GAME OVER!",
            align="center",
            font=("Courier", 30, "bold")
        )

        self.goto(0, -50)
        self.color("white")
        self.write(
            f"Your score: {self.score}",
            align="center",
            font=("Courier", 24, "normal")
        )

    @staticmethod
    def get_path():
        return path.abspath(os.path.dirname(__file__))

    def get_highscores(self):
        def sort_by_dict_value(e):
            return e["score"]

        with open(self.get_path() + "/highscores.json") as f:
            self.highscores = json.load(f)
            self.highscores.sort(key=sort_by_dict_value, reverse=True)

    def update_highscores(self, name: str, highscore: int, pos: int):
        self.highscores.pop()
        self.highscores.insert(pos, dict(name=name, score=highscore))

        with open(self.get_path() + "/highscores.json", mode="w") as f:
            json.dump(self.highscores, f)

    def rank_position(self):
        position = len(self.highscores)
        for record in self.highscores[::-1]:
            if self.score > record["score"]:
                position -= 1
            else:
                break

        return position

    def display_highscores(self):
        self.color("white")
        self.goto(0, 80)
        for pos, record in enumerate(self.highscores):
            name = f"{pos + 1}.{record['name'].upper()} ".ljust(20)
            score = str(record["score"]).rjust(3)
            self.write(
                f"{name}{score}",
                align="center",
                font=("Courier", 30, "bold")
            )
            self.goto(0, self.ycor() - 60)
