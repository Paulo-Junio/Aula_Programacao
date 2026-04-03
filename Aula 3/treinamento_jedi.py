# Treinamento Jedi
# Para se tornar um mestre do Pygame, você precisa praticar! Tente resolver estes três 
# desafios em casa antes da nossa próxima aula.

# Missão 1: O Alvo
# Crie um programa que desenhe um alvo de arco e flecha no centro da tela.
# Como fazer: Desenhe três círculos, um dentro do outro. O maior deve ser vermelho, o 
# do meio branco e o menor (o centro) vermelho novamente.
# Dica: Desenhe o círculo maior primeiro, depois o médio e por último o menor, para que 
# os menores fiquem por cima!

# Missão 2: A Bandeira
# Escolha um país que tenha uma bandeira feita apenas de retângulos (como França, Itália, 
# Alemanha ou Colômbia) e tente desenhá-la usando o Pygame.
# Como fazer: Você precisará desenhar três retângulos de cores diferentes, posicionados 
# lado a lado ou um em cima do outro.
# Dica: Calcule bem a largura e a altura de cada retângulo para que eles preencham a tela 
# perfeitamente.

# Missão 3: O Invasor Espacial (Blitting)
# Vamos usar imagens! Encontre ou desenhe uma imagem pequena de uma nave espacial ou alienígena (salve como .png ).
# Como fazer: Crie um programa que carregue essa imagem e a exiba (usando a função blit ) em quatro lugares diferentes da tela: nos quatro cantos!
# Dica: Lembre-se de usar .convert_alpha() ao carregar a imagem para que o fundo dela fique transparente.

import pygame

pygame.init()

comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Treinamento Jedi")

# Cores

VERMELHO = (255,0,0)
BRANCO = (255,255,255)
VERDE = (0,255,0)
AMARELO = (255,255,0)
AZUL = (0,0,255)


# Definido coordenadas de centro
coord = (comprimento//2, largura//2)

# Carregado imagem
img = pygame.image.load("nave.png").convert_alpha()


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        tela.fill((100,100,100))

        # Missão 1
        pygame.draw.circle(tela, VERMELHO, coord, 125)
        pygame.draw.circle(tela, BRANCO, coord, 75)
        pygame.draw.circle(tela, VERMELHO, coord, 25)

        # Missão 2
        pygame.draw.rect(tela,VERDE, [0,0, 200,140])
        pygame.draw.polygon(tela, AMARELO, [(25,70),(100,15),(175,70), (100,125),(25,70)])
        pygame.draw.circle(tela, AZUL, (100,70),35 )


        # Missão 3
        # Blit das imagens
        tela.blit(img, (100, 150))
        tela.blit(img, (726, 492))
        tela.blit(img, (574, 16))
        tela.blit(img, (654, 254))


    pygame.display.update()

pygame.quit()