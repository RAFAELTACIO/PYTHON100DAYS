
print ("BEMVINDO AO LEILAO CEGO ONLINE")
lances = {}
loop = 0
propostas = []

while True:
    nome = input("QUAL É O SEU NOME: ")
    proposta = int(input("QUAL A SUA PROPOSTA? "))
    lances[loop] = [nome, proposta]
    propostas.append(proposta)
    maispessoas = input("HÁ MAIS ALGUM COMPETIDOR S/N: ").upper()
    if maispessoas == 'S':
        print(" " * 50)
        loop += 1
    else:
        break

vencedor = lances[propostas.index(max(propostas))]
print(f'O VENCEDOR FOI {vencedor[0]} COM UM VALOR DE {vencedor[1]} REAIS')
