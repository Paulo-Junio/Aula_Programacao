# Atividade em Sala: O Dragão Teleportador (Desafio da Aula)

# Objetivo: Combinar texto, som e interatividade para controlar um personagem, reforçando 
# o uso de Rects .

# 1. Crie um personagem (pode ser uma imagem ou um retângulo simples) que se move 
# com as setas do teclado usando movimento discreto (KEYDOWN).

# 2. Ao clicar com o botão esquerdo do mouse, o personagem deve se teletransportar para 
# a posição do clique (event.pos) e tocar um efeito sonoro curto (você precisará de um 
# arquivo .wav ou .ogg na pasta assets/ ).

# 3. Exiba um título no topo da tela, como "DRAGÃO MÁGICO", usando uma fonte 
# personalizada e posicionamento com 
# get_rect() para centralizá-lo

import pygame

# Iniciando o Pygame
pygame.init()

# Criando a tela

comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("O Dragão Teleportador")


# Adicionando imagem
dragon = pygame.image.load("dragon.png").convert_alpha()
dragon_rect = dragon.get_rect()
dragon_rect.center = (comprimento//2, largura//2)


# Adicionando som
som = pygame.mixer.Sound("sound.wav")

# Adicionando fonte

font = pygame.font.Font("fonte.ttf", 45)
texto = font.render("DRAGÃO MÁGICO", True, (255,165,0))
texto_rect = texto.get_rect()
texto_rect.center= (comprimento//2, 50)


# Valores de ambiente
VELOCIDADE = 10




# Loop pygame
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCIDADE
            if evento.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCIDADE
            if evento.key == pygame.K_UP:
                dragon_rect.y -= VELOCIDADE
            if evento.key == pygame.K_DOWN:
                dragon_rect.y += VELOCIDADE
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            dragon_rect.center = evento.pos # (x, y)
            som.play()

    tela.fill((0,0,0))
    # Blita da imagem
    tela.blit(dragon,dragon_rect)

    # Blita o texto
    tela.blit(texto, texto_rect)

    pygame.display.update()
pygame.quit()