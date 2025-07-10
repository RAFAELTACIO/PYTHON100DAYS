from turtle import Turtle,Screen
import random

cores = ['red','blue','yellow','green','purple']

cores_tartarugas = {
    "vermelha": "red",
    "azul": "blue",
    "amarela": "yellow",
    "verde": "green",
    "roxa": "purple"
}
def escolhertartaruga():
    choose = input('Escolha uma tartaruga: Vermelha/Azul/Amarela/Verde/Roxa:').lower()
    if choose not in cores_tartarugas:
        print("Escolha inválida. Tente novamente.")
    else:
        cor_escolhida = cores_tartarugas[choose]
        return cor_escolhida

def checkwinner(winner, chosen):
    if winner == chosen:
        print("YOU HAVE CHOSEN RIGHT")
        print(f"THE WINNER IS: {winner.upper()}")
    else:
        print("YOU HAVE CHOSEN WRONG")
        print(f"THE WINNER IS: {winner.upper()}")

def turtlerace():
    tartarugas = []
    escolha = escolhertartaruga()
    if escolha:
        for i in range(0,len(cores)):#GERANDO OS OBJETOS
            tartarugas.append(Turtle())#GERANDO OS OBJETOS
            tartarugas[i].color(cores[i])
            tartarugas[i].shape('turtle')
            tartarugas[i].speed('fastest')

        loop = 0
        for tartaruga in tartarugas:
            tartaruga.hideturtle()
            tartaruga.penup()
            tartaruga.goto(-200,200)
            tartaruga.left(180)
            tartaruga.forward(100)
            tartaruga.left(90)
            tartaruga.forward(100*(loop+1))
            tartaruga.left(90)
            tartaruga.showturtle()
            loop = loop + 1

        race_on = True
        while race_on:
            for racer in tartarugas:
                racer.forward(random.randint(0,15))
            for racer in tartarugas:
                if racer.xcor() >= 225:
                    checkwinner(racer.color()[0], escolha)
                    race_on = False
                    break
    else:
        escolha = escolhertartaruga()

turtlerace()
screen = Screen()
screen.mainloop()


