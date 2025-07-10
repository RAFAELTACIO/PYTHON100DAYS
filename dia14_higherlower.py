
import random
famosos_seguidores = {
    "Cristiano Ronaldo": 652,
    "Lionel Messi": 505,
    "Selena Gomez": 421,
    "Dwayne Johnson": 394,
    "Kylie Jenner": 393,
    "Ariana Grande": 375,
    "Kim Kardashian": 357,
    "Beyoncé": 311,
    "Khloé Kardashian": 303,
    "Justin Bieber": 294,
    "Kendall Jenner": 288,
    "Taylor Swift": 281,
    "National Geographic": 278,
    "Virat Kohli": 272,
    "Jennifer Lopez": 248,
    "Neymar": 229,
    "Nicki Minaj": 225,
    "Kourtney Kardashian": 218,
    "Miley Cyrus": 212,
    "Katy Perry": 204,
    "Zendaya": 178,
    "Kevin Hart": 177,
    "Real Madrid": 175,
    "Cardi B": 163,
    "LeBron James": 159
}

lista_famosos = list(famosos_seguidores.items())

def sorteio():
    numerosorteado = int(random.random() * 25)
    return numerosorteado

def teste(famoso1, famoso2, pergunta):
    if pergunta == "A" and famosos_seguidores[famoso1] > famosos_seguidores[famoso2]:
        print("VOCÊ ACERTOU")
        return famoso1
    elif pergunta == "B" and famosos_seguidores[famoso2] > famosos_seguidores[famoso1]:
        print("VOCÊ ACERTOU")
        return famoso2
    else:
        print("VOCÊ ERROU")
        return False

pontuacao = 0

def atualizar_pontuacao():
    global pontuacao
    pontuacao += 1
    print(f'SUA PONTUAÇÃO É: {pontuacao}')

def higherlower():
    while True:
        if pontuacao == 0:
            famoso1 = lista_famosos[sorteio()][0]
        print("HIGHER LOWER GAME")
        while True:
            famoso2 = lista_famosos[sorteio()][0]
            if famoso2 != famoso1:
                break

        print(f"COMPARE A: {famoso1}")
        print("VERSUS")
        print(f"CONTRA B: {famoso2}")
        pergunta = input("A OU B: ").upper()
        vencedor = teste(famoso1, famoso2, pergunta)

        if vencedor == False:
            break
        else:
            famoso1 = vencedor
            atualizar_pontuacao()

while True:
    higherlower()
    jogarnovamente = input("VOCE QUER JOGAR DE NOVO? S/N").upper()
    if jogarnovamente != "S":
        break
