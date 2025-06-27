
import random
def moedagens():
    contagem = 0

    while True:
        acerte = input("VAI SER CARA OU COROA? CARA/COROA: ").upper()
        moeda = int(random.random() * 10)

        if (moeda % 2 == 0 and acerte == "CARA") or (moeda % 2 == 1 and acerte == "COROA"):
            contagem += 1
            print("VOCÊ ACERTOU")
        else:
            print("VOCÊ ERROU")

        print("ACERTOS:", contagem)

        jogar_novamente = input("Quer jogar de novo? (S/N): ").upper()
        if jogar_novamente != "S":
            print("Jogo encerrado.")
            break

moedagens()
