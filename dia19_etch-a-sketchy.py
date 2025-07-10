from turtle import Turtle, Screen

timotio = Turtle()
screen = Screen()
timotio.speed('fastest')

def moveforward():
    timotio.forward(40)

def movebackward():
    timotio.backward(40)

def moveleft():
    timotio.left(18)

def moveright():
    timotio.right(18)

def cleanscreen():
    timotio.penup()
    timotio.hideturtle()
    timotio.goto(0, 0)
    timotio.clear()
    timotio.showturtle()
    timotio.pendown()

screen.listen()
screen.onkey(key ='Up', fun=moveforward)
screen.onkey(key ='Down', fun=movebackward)
screen.onkey(key ='Left', fun=moveleft)
screen.onkey(key ='Right', fun=moveright)
screen.onkey(key ='c', fun=cleanscreen)

screen.mainloop()