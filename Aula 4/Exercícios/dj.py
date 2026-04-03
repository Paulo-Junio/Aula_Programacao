# Atividade de Casa 1: O DJ do Jogo
# Objetivo: Explorar o módulo diferença entre mixer com múltiplos sons e controle de música, aplicando a 
# Sound e  Music .

# 1. Escolha 3 efeitos sonoros diferentes (ex: pulo, tiro, explosão) e 2 músicas de fundo (uma para o "jogo" e outra para o "menu"). 

# 2. Implemente: 
# Um botão (pode ser um retângulo na tela) que, ao ser clicado com o mouse, troca a música de fundo entre as duas 
# opções (pygame.mixer.music.play(-1) ) pygame.mixer.music.load() e 

# Três teclas diferentes (ex: 'A', 'S', 'D') que, ao serem pressionadas, tocam um dos efeitos 
# sonoros ( pygame.mixer.Sound().play() ).

# Um texto na tela que indica qual música está tocando no momento, atualizando-o quando a música muda

import pygame

# Iniciando pygame
pygame.init()

# Criando a tela

comprimento = 800
largura = 400

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("O DJ do Jogo")

# Adicionando cores e retângulo

VERMELHO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
BRANCO = (255,255,255)
PRETO = (0,0,0)

botao_rect = pygame.Rect(300,250,200,60)


# Adicionando sons e músicas

som_1 = pygame.mixer.Sound("sound.wav")
som_2 = pygame.mixer.Sound("sound2.wav")
som_3 = pygame.mixer.Sound("sound3.wav")

musica_menu = "music.wav"
musica_jogo = "music2.wav"

pygame.mixer.music.load(musica_menu)
pygame.mixer.music.play(-1)


# Adicionando texto
font = pygame.font.Font("fonte.ttf", 45)
fonte = pygame.font.SysFont("calibri", 20, True)
musica_atual = "Menu"

# Adicionando clock
clock = pygame.time.Clock()
FPS = 60

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_rect.collidepoint(evento.pos):
                if musica_atual == "Menu":
                    pygame.mixer.music.load(musica_jogo)
                    musica_atual = "Jogo"
                else:
                    pygame.mixer.music.load(musica_menu)
                    musica_atual = "Menu"
                pygame.mixer.music.play(-1)
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                som_1.play()
            if evento.key == pygame.K_s:
                som_2.play()
            if evento.key == pygame.K_d:
                som_3.play()
    tela.fill(BRANCO)

    # Criando o botão (retêngulo)
    pygame.draw.rect(tela, AZUL, botao_rect)
    texto_botao = fonte.render("Mudar de música", True, BRANCO)
    tela.blit(texto_botao, (botao_rect.x + 30, botao_rect.y + 20))

    # Texto da música
    texto = font.render(f"Música Atual: {musica_atual}", True, PRETO)
    tela.blit(texto, (200,150))





    pygame.display.update()
    clock.tick(FPS)
pygame.quit()