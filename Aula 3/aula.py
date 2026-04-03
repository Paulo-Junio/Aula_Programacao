# Importar a biblioteca
import pygame


# Iniciar o pygame
pygame.init()


# Criar a minha

comprimento = 800
largura = 600

tela = pygame.display.set_mode(  (comprimento, largura)   )
pygame.display.set_caption("Minha primeira tela")

# Criando as cores
# ------ RGB -> VERMELHO, VERDE , AZUL
VERMELHO = (255,0,0)

VERDE = (0,255,0)

AZUL = (0,0,255)

PRETO = (0,0,0)

BRANCO = (255,255,255)

AMARELO = (255,255,0)

# Preparando a imagem

img = pygame.image.load("dragon_right.png")
img_rect = img.get_rect()
img_rect.topright = (500,25)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Blitar da imagem na tela
    tela.fill((0,0,0))
    tela.blit(img, img_rect)

     # Desehando um retângulo  
    #                                [X,  Y, COMPRIMENTO, LARGURA]     
    pygame.draw.rect(tela, VERMELHO, [200,150, 100, 50]) 
    
    # Desenhado circulo
    pygame.draw.circle(tela, AZUL, (400,300), 50)

    # Desenho linha
    pygame.draw.line(tela, VERDE, (10,400), (500,450), 3)

    pygame.draw.arc(tela, BRANCO,  [600,500, 100, 50], 25.0,40.0, 1)
    pygame.draw.polygon(tela, AMARELO, [(200,300), (400, 150),(600,300),(400, 450), (200,300) ])


    pygame.display.update()

            

pygame.quit()