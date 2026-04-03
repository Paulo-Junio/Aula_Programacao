## Atividade 2: A "Roleta de Loot" (Focada em Listas e For) 
#   Esta atividade é ótima para fixar o conceito de listas e o comando for. 
#       • A Missão: O jogador abriu um baú do tesouro. Eles precisam criar uma lista 
#           chamada bau com 5 itens divertidos (ex: "Moeda de Ouro", "Bota Velha", 
#           "Poção de Vida", "Espada Enferrujada", "Diamante"). 
#
#       • A Ação: Usar um loop for para percorrer a lista e imprimir na tela, com um 
#           suspense: "Vasculhando o baú... Você encontrou um(a) [item da lista]!". 
#
#       • O Twist (Condicionais): Usar um if dentro do for. Se o item for "Bota Velha", 
#           o programa deve imprimir "Eca, lixo!". Se for "Diamante", imprimir "JACKPOT!".

import random
lista = ["Moeda de Ouro", "Bota Velha", "Poção de Vida", "Espada Enferrujada", "Diamante"]
bau = random.sample(lista, len(lista))

for i in bau:
    print(f"Vasculhando o baú... Você encontrou um(a) {i} !")

    if( i == "Bota Velha" or i == "Espada Enferrujada" ):
        print(f"Eca, lixo! Jogando a {i} fora.")
    elif  (i =="Diamante" ):
        print(f"JACKPOT! Você achou um {i}. Tá rico!!")
    else:
        print(f"Guardando a {i} na mochila")
    print("---"*20)
