## Desafio prático: O "Simulador de Combate Aleatório" 
#      • Passo 1 (Variáveis e Tipos): 
#          Crie as variáveis principais do jogador: vida (ex: 3) e pontos (inicialmente 0). 
#      • Passo 2 (Aleatoriedade): 
#          Simule dois eventos aleatórios a cada rodada: 
#               • Defesa: pode ser defendeu ou foi acertado. 
#               • Ataque: pode ser deu dano ou não deu dano. 
#       • Passo 3 (Condicionais): 
#           Use estruturas if/else para definir as regras:
#               • Se foi acertado, subtraia 1 da vida. 
#               • Se o ataque der dano, adicione 10 pontos. 
#       • Passo 4 (Loops): 
#           Coloque tudo dentro de um loop for que repita 7 vezes (rodadas). 
#       • Passo 5 (Condições de Fim): 
#            • Se a vida chegar a zero, exiba "Você perdeu!" e encerre o loop. 
#            • Se completar todas as rodadas com vida 

import random

vida = 5
pontos = 0

for i in range(7):
    ataque = random.choice(["Deu dano", "Não deu dano"])
    defesa = random.choice(["Defendeu", "Foi acertado"])

    if (defesa == "Foi acertado"):
        vida -= 1

    if (ataque == "Deu dano"):
        pontos += 10

    if (vida <= 0):
        print("Você perdeu!")
        break

if (vida > 0):
    print("Você ganhou!")
    print(f"Total de pontos: {pontos}")
