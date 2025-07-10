from score import ScoreBoard
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key ="Left", fun=snake.left)
screen.onkey(key ="Right", fun=snake.right)
screen.onkey(key ="Up", fun=snake.up)
screen.onkey(key ="Down", fun=snake.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extendSnake()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()
screen.mainloop()
