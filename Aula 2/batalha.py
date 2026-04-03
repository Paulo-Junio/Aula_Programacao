## Atividade 1: O "Simulador de Batalha" (Expansão do seu desafio final)  
#       • Passo 1 (Variáveis e Tipos): Peça para criarem as variáveis do jogador 
#           (nome, vida, poder_ataque) e do chefão (nome_chefe, vida_chefe). 
#
#       • Passo 2 (Operadores e Condicionais): Eles devem simular um ataque. 
#           Subtrair o poder_ataque da vida_chefe. Depois, usar if/else para checar: Se 
#           a vida do chefe for menor ou igual a zero, imprimir "Você derrotou o monstro!". 
#           Senão, imprimir "O monstro ainda está de pé!". 
#
#       • Passo 3 (Loops): Desafie os mais rápidos a colocar isso dentro de um loop 
#           while: "Enquanto a vida do chefe for maior que zero, continue atacando".


nome = input("Escolha o nome do seu campeão: ")
poder_ataque = 25

chefao = "Darius"
vida_chefe = 100

while (vida_chefe > 0):
    vida_chefe -= poder_ataque

    if(vida_chefe > 0):
        print(f"O {chefao} ainda está de pé!")
    else:
        print(f"Você derrotou o {chefao}!")
