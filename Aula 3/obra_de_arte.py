##  A Primeira Obra de Arte
# Seu objetivo é criar um programa em Python usando Pygame que desenhe uma cena 
# simples na tela. Siga os passos abaixo:

# 1.A Tela de Pintura: Crie uma janela com o tamanho de 800 pixels de largura por 600 
# pixels de altura. Dê a ela o título "Minha Primeira Obra de Arte".

# 2.O Fundo: Preencha o fundo da tela com uma cor de sua escolha (diferente de preto). 
# Lembre-se de usar o formato RGB, por exemplo: (135, 206, 235) para um azul céu.

# 3.O Chão (Retângulo): Desenhe um retângulo verde na parte inferior da tela para 
# representar o chão. Ele deve começar no lado esquerdo (x=0) e ir até o lado direito 
# (comprimento=800).

# 4.O Sol (Círculo): Desenhe um círculo amarelo no canto superior direito da tela para 
# representar o sol.

# 5.A Casa (Retângulo e Linhas): Desenhe um quadrado (que é um retângulo com lados 
# iguais) no centro da tela para ser a base de uma casa. Em seguida, use a função de 
# desenhar linhas (pygame.draw.line) para fazer o telhado em formato de triângulo.

# 6.O Personagem (Imagem): Tente carregar e exibir uma imagem de personagem em 
# qualquer lugar da tela. (Você pode usar uma imagem que já tenha ou criar uma 
# simples).

# Dica de Ouro: Lembre-se que o ponto (0,0) fica no canto superior esquerdo! Para mover 
# algo para baixo, aumente o valor de Y. Para mover para a direita, aumente o valor de X.

import pygame

# Iniciar o pygame
pygame.init()

# Criar minha tela

comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Minha Primeira Obra de Arte")

AZUL_CEU = (135, 206, 235)
VERDE = (0,240, 100)
AMARELO = (255,255,0)
MARROM = (150,75,0)
ROSA = (255, 192,203)

# Carregando imagem
img = pygame.image.load("flor.png").convert_alpha()
img_rect = img.get_rect()
img_rect.bottomright = (725,570)



# Loop principal do pygame
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(AZUL_CEU)

    # Fazer o chão
    pygame.draw.rect(tela, VERDE, [0,570, 800, 30])   

    # Fazer o sol
    pygame.draw.circle(tela, AMARELO, (650,150),75,)

    # Fazer a casa
    pygame.draw.rect(tela, ROSA, [350,470, 100,100])
    pygame.draw.polygon(tela, MARROM, [(340,470),(400,440),(460,470),(340,470)])


    # Blit da imagem
    tela.blit(img, img_rect)

    pygame.display.update()

pygame.quit()