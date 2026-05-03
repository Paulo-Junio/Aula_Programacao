import pygame
import random

# Iniciar o pygame
pygame.init()

# Criar a tela
comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Aula 5: Movimentos contínuos")


# Cores
VERMELHO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
PRETO = (0,0,0)
BRANCO = (255,255,255)

# Personagem
personagem_rect = pygame.Rect(300,250,30,30) #[300,250,75,75]
obstaculo_rect = pygame.Rect(457,512,30,30)
# Som
som = pygame.mixer.Sound("sound_1.wav")

# Valores de ambiente
VELOCIDADE = 10

# Clock

clock = pygame.time.Clock()
FPS = 60
# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Captura do estado do teclado
    keys = pygame.key.get_pressed()
    
    # Verfica tecla apertada e move o personagem
    if keys[pygame.K_LEFT]:
        personagem_rect.x -= VELOCIDADE
    if keys[pygame.K_RIGHT]:
        personagem_rect.x += VELOCIDADE
    if keys[pygame.K_UP]:
        personagem_rect.y -= VELOCIDADE
    if keys[pygame.K_DOWN]:
        personagem_rect.y += VELOCIDADE 


    # Restrição horizontal
    if personagem_rect.left < 0:
        personagem_rect.left = 0
    if personagem_rect.right > comprimento:
        personagem_rect.right = comprimento
    
    # Restrição Vertical
    if personagem_rect.top < 0:
        personagem_rect.top = 0
    if personagem_rect.bottom > largura:
        personagem_rect.bottom = largura

    if personagem_rect.colliderect(obstaculo_rect):
        som.play()
        obstaculo_rect.x = random.randint(0, comprimento - 30)
        obstaculo_rect.y = random.randint(30, largura - 30)
        



    tela.fill(BRANCO)
    pygame.draw.rect(tela, VERMELHO,personagem_rect)
    pygame.draw.rect(tela, AZUL,obstaculo_rect)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()