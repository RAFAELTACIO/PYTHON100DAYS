
import random
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
valoresdascartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def contagem(cartaspassadas):
    valordascartascontagem = 0
    for i in cartaspassadas:
        valordascartascontagem += valoresdascartas[cartas.index(i)]
    if "A" in cartaspassadas and valordascartascontagem > 21:
        valordascartascontagem = 0
        for i in cartaspassadas:
            if i == "A":
                valordascartascontagem += 1
            else:
                valordascartascontagem += valoresdascartas[cartas.index(i)]
        return valordascartascontagem
    else:
        return valordascartascontagem

def contagemfinal(valordascartasmaquina, valordascartasjogador):
    if valordascartasjogador > valordascartasmaquina:
        print("VOCÊ VENCEU!")
    elif valordascartasmaquina > valordascartasjogador:
        print("VOCÊ PERDEU!")
    else:
        print("EMPATOU")

def sorteiodecartas(numerodecartas):
    cartasdavez = [random.choice(cartas) for k in range(numerodecartas)]
    return cartasdavez

def blackjack():
    loop = 0
    while True:
        if loop == 0:
            cartasjogador = sorteiodecartas(2)
            valordascartasjogador = contagem(cartasjogador)
            cartasmaquina = sorteiodecartas(1)
            valordascartasmaquina = contagem(cartasmaquina)
            print(f"SUAS CARTAS SÃO: {cartasjogador} E SUA PONTUAÇÃO É {valordascartasjogador}")
            print(f"VALOR DA PRIMEIRA CARTA DO COMPUTADOR: {valordascartasmaquina}")

        maiscartas = input("DIGITE S PARA MAIS UMA CARTA E N PARA PASSAR").upper()
        if maiscartas == "S":
            loop = 1
            cartasjogador.append(random.choice(cartas))
            valordascartasjogador = contagem(cartasjogador)
            print(f"SUAS CARTAS SÃO: {cartasjogador} E SUA PONTUAÇÃO É {valordascartasjogador}")
            if valordascartasjogador > 21:
                print("VOCE PERDEU!")
                break
        else:
            loop = 1
            cartasmaquina.append(random.choice(cartas))
            valordascartasmaquina = contagem(cartasmaquina)
            if valordascartasmaquina < 16:
                cartasmaquina.append(random.choice(cartas))
                valordascartasmaquina = contagem(cartasmaquina)
            if valordascartasmaquina > 21:
                print("VOCÊ VENCEU!")
                break
            else:
                print(f"VALOR DAS CARTAS DO COMPUTADOR É: {valordascartasmaquina}")
                contagemfinal(valordascartasmaquina, valordascartasjogador)
                break

    maisumaescolha = input("VOCE QUER JOGAR DENOVO? S/N").upper()
    if maisumaescolha == "S":
        blackjack()

blackjack()
