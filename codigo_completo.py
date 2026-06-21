import random
lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
cartas = {"c1": None, "c2": None, "c3": None, "c4": None, "c5": None}
valormao = {"nada": 0, "um par": 1, "dois par": 2, "trinca": 3, "full house": 4, "quadra": 5, "quina": 6,
}
########################
# defs
def trocar_carta(nome, dicionario):
    cartas[nome] = random.choice(dicionario)

def contar_repetido(cartas):
    contagem = {}
    for valor in cartas.values():
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
    return contagem

def analisar_mao(cartas):
    contagem = contar_repetido(cartas)
    quantidades = list(contagem.values())
    if 5 in quantidades:
        return "quina"
    elif 4 in quantidades:
        return "quadra"
    elif 3 in quantidades and 2 in quantidades:
        return "full house"
    elif 3 in quantidades:
        return "trinca"
    elif quantidades.count(2) == 2:
        return "dois par"
    elif 2 in quantidades:
        return "um par"
    else:
        return "nada"

def mostra_mao():
    print(*cartas.values())

#######################
# jogador1
for i in range(1, 6):
    trocar_carta(f"c{i}", lista)

print("mao1", end=" ")
mostra_mao()
print(contar_repetido(cartas))
contagem = contar_repetido(cartas)
#############################3
for carta, quantidade in contagem.items():
    if quantidade > 2 or quantidade == 2:
        print(f"sua carta {carta} apareceu {quantidade} vezes")

print(analisar_mao(cartas))
tipo_mao = analisar_mao(cartas)
####################
for carta, quantidade in contagem.items():
    if quantidade > 2 or quantidade == 2:
        valor_tipo = carta
    else:
        valor_tipo = 0

mao1 = (tipo_mao, valor_tipo)
jogador1 = mao1
#########################
# jogador2
for i in range(1, 6):
    trocar_carta(f"c{i}", lista)

print("mao2", end=" ")
mostra_mao()
print(contar_repetido(cartas))
contagem = contar_repetido(cartas)
for carta, quantidade in contagem.items():
    if quantidade > 2 or quantidade == 2:
        print(f"sua carta {carta} apareceu {quantidade} vezes")

print(analisar_mao(cartas))
tipo_mao = analisar_mao(cartas)
for carta, quantidade in contagem.items():
    if quantidade > 2 or quantidade == 2:
        valor_tipo = carta
    else:
        valor_tipo = 0

mao2 = (tipo_mao, valor_tipo)
jogador2 = mao2
##########################
print("jogador ganhador e:")
if valormao[jogador1[0]] == valormao[jogador2[0]]:
    if jogador1[1] > jogador2[1]:
        print("jogador1 valor")
    else:
        print("jogador2 valor")
elif valormao[jogador1[0]] > valormao[jogador2[0]]:
    print("jogador1")
elif valormao[jogador1[0]] < valormao[jogador2[0]]:
    print("jogador2")
#######################