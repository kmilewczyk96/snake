import time
from turtle import Screen

from menu import Menu
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.title("SNAKE")
screen.setup(width=800, height=800)


def start_main_menu():
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0)
    main_menu = Menu(start=start_game, highscores=highscores, quit=screen.bye)
    screen.listen()
    screen.onkey(key="Up", fun=main_menu.up)
    screen.onkey(key="Down", fun=main_menu.down)
    screen.onkey(key="space", fun=main_menu.trigger)

    while True:
        screen.update()


def start_game():
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0)
    screen.update()

    snake = Snake()
    score = Score()
    food = Food()

    screen.listen()
    screen.onkey(key="w", fun=snake.head_north)
    screen.onkey(key="s", fun=snake.head_south)
    screen.onkey(key="a", fun=snake.head_west)
    screen.onkey(key="d", fun=snake.head_east)

    run = True
    while run:
        screen.update()
        time.sleep(0.04)
        snake.move()

        if snake.head.distance(food) < 10:
            snake.grow()
            score.score += 1
            screen.title(f"CURRENT SCORE: {score.score}")
            food.spawn()

        if (
                snake.head.xcor() > 390 or
                snake.head.xcor() < -390 or
                snake.head.ycor() > 390 or
                snake.head.ycor() < -390
        ):
            death_animation(snake)
            run = False

        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                death_animation(snake)
                run = False

    result(score)


def result(score):
    screen.clearscreen()
    screen.bgcolor("black")
    score.result()
    if score.rank_position() < len(score.highscores):
        name = ''
        valid = False
        while not valid:
            name = screen.textinput(
                title="IMPRESSIVE SCORE!",
                prompt="Please enter your name (2 - 10 characters)")
            if name and len(name) in range(3, 11):
                valid = True

        if name:
            score.update_highscores(name, score.score, score.rank_position())

    screen.listen()
    screen.onkey(key="space", fun=highscores)

    time.sleep(2)
    highscores()


def highscores():
    screen.clearscreen()
    screen.bgcolor("black")
    screen.tracer(0)
    screen.update()
    score = Score()
    score.display_highscores()
    screen.update()

    screen.listen()
    screen.onkey(key="space", fun=start_main_menu)


def exit_game():
    screen.bye()


def death_animation(snake):
    for i in range(5):
        snake.hide_snake()
        screen.update()
        time.sleep(0.1)
        snake.show_snake()
        screen.update()
        time.sleep(0.1)


if __name__ == '__main__':
    start_main_menu()
    screen.mainloop()
