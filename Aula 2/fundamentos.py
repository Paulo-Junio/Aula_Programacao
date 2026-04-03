## Fundamentos de Python

# Variáveis

## "Caixa" que guarda valores


inteiros = 1 # int -> 1, 2, 3, 4 ...
decimais = 0.5 # float -> 0.5, 1.2, 5.0 
booleanos = True # bool -> True, False


# Operações Matemáticas 

soma = 1 + 2 # 3
subtracao = 3 - 1 # 2
multiplicacao = 2 * 2 # 4
exp =  2 ** 2 # 4 
divisao = 9 / 2 # 4.5
divisao_int = 9 // 2 # 4
divisao_resto = 9 % 2 # 1

# Comparação 

# == -> Igualdade
# != -> Diferente
# > -> Maior que
# < -> Menor que
# >= -> Maior ou igual que
# <= -> Menor ou igual que

# Condicionais 

# if -> Se
# elif -> Senão se
# else -> Senão

nome = "João"

if (nome == "Davi"): 
    print( "Nome é Davi")
elif (nome =="Rafael"):
    print( "Nome é Rafael")
elif (nome == "Maria"):
    print("Nome é Maria")
else: 
    print("Não conheço")


# Lista
#----------0--------1-------2--------3
lista = [ "Paulo","Davi", "Ellen", "Maria", "Rafael"]

# Loops de Repetição 
## Permitem executar um bloco de código mais de uma vez

def loop_while(nome): 
    print("To na função loop_while")
    print(f"Nome é {nome}")
    print("=" * 20)
    numero = input("Fala um número: ")

    return numero


while (nome != "Jorge"):
    nome = input("Digite um nome:")
    num = loop_while(nome)
    print(f"O numero é {num}")
print("Saiu do loop WHILE")


