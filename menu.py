from turtle import Turtle


class Menu(Turtle):
    def __init__(self, **actions):
        super().__init__(shape="square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.index = 0
        self.actions = actions
        self.action_names = list(actions.keys())
        self.goto(0, (30 * len(self.action_names)))
        self.gap = 400 // len(self.action_names)
        self.draw_menu()

    def up(self):
        if self.index > 0:
            self.index -= 1
            self.goto(0, self.ycor() + self.gap)
            self.shapesize(stretch_wid=0.2, stretch_len=(1.5 * len(self.action_names[self.index])))

    def down(self):
        if self.index < len(self.actions) - 1:
            self.index += 1
            self.goto(0, self.ycor() - self.gap)
            self.shapesize(stretch_wid=0.2, stretch_len=(1.5 * len(self.action_names[self.index])))

    def trigger(self):
        self.actions[self.action_names[self.index]]()

    def draw_menu(self):
        for action in self.action_names:
            self.write(action.upper(), align="center", font=("Cursor", 32, "bold"))
            self.goto(0, self.ycor() - self.gap)

        self.goto(0, (30 * len(self.action_names)))
        self.shapesize(stretch_wid=0.2, stretch_len=(len(self.action_names[self.index]) + 2))
