
import random

def adivinhacao():
    numerosecreto = random.randint(0, 100)
    dificuldade = input("VOCE QUER QUE A DIFICULDADE SEJA FACIL OU DIFICIL? F/D").upper()
    if dificuldade == "F":
        vidas = 10
    elif dificuldade == "D":
        vidas = 5
    while True:
        if vidas == 0:
            print("VOCE PERDEU")
            break
        else:
            print(f"VOCE TEM {vidas} VIDAS")
            teste = int(input("DIGITE UM NUMERO ENTRE 0 E 100: "))
            if teste == numerosecreto:
                print("VOCE VENCEU")
                break
            elif teste > numerosecreto:
                if abs(teste - numerosecreto) > 25:
                    vidas -= 1
                    print("MUITO ALTO")
                else:
                    vidas -= 1
                    print("ALTO")
            elif teste < numerosecreto:
                if abs(teste - numerosecreto) > 25:
                    vidas -= 1
                    print("MUITO BAIXO")
                else:
                    vidas -= 1
                    print("BAIXO")

while True:
    adivinhacao()
    jogarnovamente = input("VOCE QUER JOGAR DE NOVO? S/N").upper()
    if jogarnovamente != "S":
        break
