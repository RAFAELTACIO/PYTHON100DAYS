<<<<<<< HEAD
import random
from turtle import *

from adodbapi.ado_consts import directions

cores = [
    "purple2", "salmon1", "SkyBlue", "snow4", "thistle4", "wheat3",
    "purple3", "salmon2", "SkyBlue1", "SpringGreen", "tomato", "wheat4",
    "purple4", "salmon3", "SkyBlue2", "SpringGreen1", "tomato1",
    "red", "salmon4", "SkyBlue3", "SpringGreen2", "tomato2",
    "red1", "SandyBrown", "SkyBlue4", "SpringGreen3", "tomato3", "yellow",
    "red2", "SeaGreen", "SlateBlue", "SpringGreen4", "tomato4", "yellow1",
    "red3", "SeaGreen1", "SlateBlue1", "SteelBlue", "turquoise", "yellow2",
    "red4", "SeaGreen2", "SlateBlue2", "SteelBlue1", "turquoise1", "yellow3",
    "RosyBrown", "SeaGreen3", "SlateBlue3", "SteelBlue2", "turquoise2", "yellow4",
    "RosyBrown1", "SeaGreen4", "SlateBlue4", "SteelBlue3", "turquoise3", "YellowGreen",
    "RosyBrown2", "seashell", "SlateGray", "SteelBlue4", "turquoise4", "RosyBrown3",
    "seashell1", "SlateGray1", "tan", "violet", "RosyBrown4", "seashell2",
    "SlateGray2", "tan1", "VioletRed", "RoyalBlue", "seashell3", "SlateGray3",
    "tan2", "VioletRed1", "RoyalBlue1", "seashell4", "SlateGray4", "tan3",
    "VioletRed2", "RoyalBlue2", "sienna", "SlateGrey", "tan4", "VioletRed3",
    "RoyalBlue3", "sienna1", "snow", "thistle", "VioletRed4", "RoyalBlue4",
    "sienna2", "snow1", "thistle1", "wheat", "SaddleBrown", "sienna3",
    "snow2", "thistle2", "wheat1", "salmon", "sienna4", "snow3",
    "thistle3", "wheat2"
]

timotio = Turtle()
timotio.shape("turtle")
timotio.speed("fast")


def positionturtle(x,y):
    timotio.hideturtle()
    timotio.penup()
    timotio.goto(x, y)
    timotio.pendown()
    timotio.showturtle()

def damienhirst():
    positionturtle(-700, 400)
    timotio.pensize(40)
    timotio.speed("fastest")
    for i in range(1,10):
        for traco in range(1,16):
            timotio.color(random.choice(cores))
            timotio.pendown()
            timotio.forward(1)
            timotio.penup()
            if traco !=15:
                timotio.forward(100)
        if i < 9:
            timotio.hideturtle()
            timotio.penup()
            timotio.left(90)
            timotio.forward(100)
            timotio.left(90)
            timotio.forward(1414)
            timotio.left(180)
            timotio.showturtle()
            print(i)
#damienhirst()

def randomwalk():
    timotio.pensize(15)
    for i in range(1,len(cores)):
        timotio.color(random.randint(0, 255) / 255,random.randint(0, 255) / 255,random.randint(0, 255) / 255)
        timotio.forward(random.randint(1,2)*50)
        timotio.left(random.randint(1,4)*90)

randomwalk()

screen = Screen()
screen.screensize(600, 400)
screen.bgcolor('white')
screen.mainloop()

=======
import random
from turtle import *

from adodbapi.ado_consts import directions

cores = [
    "purple2", "salmon1", "SkyBlue", "snow4", "thistle4", "wheat3",
    "purple3", "salmon2", "SkyBlue1", "SpringGreen", "tomato", "wheat4",
    "purple4", "salmon3", "SkyBlue2", "SpringGreen1", "tomato1",
    "red", "salmon4", "SkyBlue3", "SpringGreen2", "tomato2",
    "red1", "SandyBrown", "SkyBlue4", "SpringGreen3", "tomato3", "yellow",
    "red2", "SeaGreen", "SlateBlue", "SpringGreen4", "tomato4", "yellow1",
    "red3", "SeaGreen1", "SlateBlue1", "SteelBlue", "turquoise", "yellow2",
    "red4", "SeaGreen2", "SlateBlue2", "SteelBlue1", "turquoise1", "yellow3",
    "RosyBrown", "SeaGreen3", "SlateBlue3", "SteelBlue2", "turquoise2", "yellow4",
    "RosyBrown1", "SeaGreen4", "SlateBlue4", "SteelBlue3", "turquoise3", "YellowGreen",
    "RosyBrown2", "seashell", "SlateGray", "SteelBlue4", "turquoise4", "RosyBrown3",
    "seashell1", "SlateGray1", "tan", "violet", "RosyBrown4", "seashell2",
    "SlateGray2", "tan1", "VioletRed", "RoyalBlue", "seashell3", "SlateGray3",
    "tan2", "VioletRed1", "RoyalBlue1", "seashell4", "SlateGray4", "tan3",
    "VioletRed2", "RoyalBlue2", "sienna", "SlateGrey", "tan4", "VioletRed3",
    "RoyalBlue3", "sienna1", "snow", "thistle", "VioletRed4", "RoyalBlue4",
    "sienna2", "snow1", "thistle1", "wheat", "SaddleBrown", "sienna3",
    "snow2", "thistle2", "wheat1", "salmon", "sienna4", "snow3",
    "thistle3", "wheat2"
]

timotio = Turtle()
timotio.shape("turtle")
timotio.speed("fast")


def positionturtle(x,y):
    timotio.hideturtle()
    timotio.penup()
    timotio.goto(x, y)
    timotio.pendown()
    timotio.showturtle()

def damienhirst():
    positionturtle(-700, 400)
    timotio.pensize(40)
    timotio.speed("fastest")
    for i in range(1,10):
        for traco in range(1,16):
            timotio.color(random.choice(cores))
            timotio.pendown()
            timotio.forward(1)
            timotio.penup()
            if traco !=15:
                timotio.forward(100)
        if i < 9:
            timotio.hideturtle()
            timotio.penup()
            timotio.left(90)
            timotio.forward(100)
            timotio.left(90)
            timotio.forward(1414)
            timotio.left(180)
            timotio.showturtle()
            print(i)
#damienhirst()

def randomwalk():
    timotio.pensize(15)
    for i in range(1,len(cores)):
        timotio.color(random.randint(0, 255) / 255,random.randint(0, 255) / 255,random.randint(0, 255) / 255)
        timotio.forward(random.randint(1,2)*50)
        timotio.left(random.randint(1,4)*90)

randomwalk()

screen = Screen()
screen.screensize(600, 400)
screen.bgcolor('white')
screen.mainloop()

>>>>>>> bc3c9ccd99c84d30a2ffd9018f001e80e152ed8c
