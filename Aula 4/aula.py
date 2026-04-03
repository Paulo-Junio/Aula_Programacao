import pygame

# Iniciando pygame
pygame.init()


# Criando a tela
comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Aula 4")

# Baixar sons
som_1 = pygame.mixer.Sound("sound_1.wav")
som_2 = pygame.mixer.Sound("sound_2.wav")

# # Tocando os sons
# som_1.play()
# pygame.time.delay(2000)
# som_2.set_volume(0.1)
# som_2.play()


# Baixando a música
# pygame.mixer.music.load("music.wav")

# # Tocando a música
# pygame.mixer.music.play(-1,0.0)
# pygame.time.delay(2000)
# som_1.play()
# pygame.time.delay(2000)
# som_2.play()
# pygame.time.delay(2000)
# pygame.mixer.music.stop()

verde = (0,255,0)
vermelho = (255,0,0)

# fonte = pygame.font.get_fonts()
# # Adicionando fontes e textos
# sistema = pygame.font.SysFont("calibri", 64, bold= False,italic=True)
# customizada = pygame.font.Font("AttackGraffiti.ttf",32)

# # Adicionando textos
# texto_sistema = sistema.render("Meu primeiro texto",True, verde,vermelho )
# sistema_rect = texto_sistema.get_rect()
# sistema_rect.center = (comprimento//2, largura//2)


# custo_texto = customizada.render("Meu segundo texto", True, vermelho)
# custo_rect = custo_texto.get_rect()
# custo_rect.center = (comprimento//2, largura//2 + 100)


# Velocida
VELOCIDADE = 10

imagem = pygame.image.load("dragon_right.png").convert_alpha()
imagem_rect = imagem.get_rect()
imagem_rect.centerx = comprimento//2
imagem_rect.bottom = largura



# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type  == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                imagem_rect.x -= VELOCIDADE
            if evento.key == pygame.K_RIGHT:
                imagem_rect.x += VELOCIDADE
            if evento.key == pygame.K_UP:
                imagem_rect.y -= VELOCIDADE
            if evento.key == pygame.K_DOWN:
                imagem_rect.y += VELOCIDADE

            # Movimento com o MOUSE
        # if evento.type == pygame.MOUSEBUTTONDOWN: 
        #     # pos = (x,y)
        #     mouse_x = evento.pos[0]
        #     mouse_y = evento.pos[1]

        #     imagem_rect.centerx = mouse_x
        #     imagem_rect.centery = mouse_y

        # if evento.type == pygame.MOUSEMOTION: 
        #     # pos = (x,y)
        #     mouse_x = evento.pos[0]
        #     mouse_y = evento.pos[1]

        #     imagem_rect.centerx = mouse_x
        #     imagem_rect.centery = mouse_y


        # if evento.type == pygame.MOUSEMOTION and evento.buttons[0] == 1: 
        #     # pos = (x,y)
        #     print(evento.buttons)
        #     mouse_x = evento.pos[0]
        #     mouse_y = evento.pos[1]

        #     imagem_rect.centerx = mouse_x
        #     imagem_rect.centery = mouse_y

    tela.fill((0,0,0))
    # # Blit da texto
    # tela.blit(texto_sistema, sistema_rect)
    # tela.blit(custo_texto, custo_rect)

    # Blit da imagem
    tela.blit(imagem, imagem_rect)
    
    pygame.display.update()

pygame.quit()