from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
        self.increase_score()

    def gameover(self):
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

