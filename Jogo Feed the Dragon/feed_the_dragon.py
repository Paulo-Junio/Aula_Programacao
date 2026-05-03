import pygame
import random

pygame.init()

# =========================
# Criação da tela
# =========================
# Defina:
# - largura da tela (ex: 1000)
# - altura da tela (ex: 400)

comprimento = 1000
largura = 400

# Crie a janela com:
# pygame.display.set_mode()
# Defina o título com:
# pygame.display.set_caption()

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Feed the Dragon")


# =========================
# Clock
# =========================
# Defina o FPS (ex: 60)
# Crie o clock com pygame.time.Clock()

FPS = 60
clock = pygame.time.Clock()

# =========================
# Variáveis do jogo
# =========================
# Defina:
# - vidas iniciais do jogador
# - velocidade do jogador
# - velocidade inicial da moeda
# - aceleração da moeda
# - distância de buffer (spawn fora da tela)
#
# Crie também:
# - pontuação
# - vidas atuais
# - velocidade atual da moeda

vidas_iniciais = 3
velocidade_jogador = 5
velocidade_inicial_moeda = 5
aceleracao = 1
buffer = 100

pontuacao = 0
vidas_atuais = vidas_iniciais
velocidade_atual_moeda = velocidade_inicial_moeda


# =========================
# Cores
# =========================
# Defina cores como:
# PRETO, BRANCO, VERDE...

PRETO = (0,0,0)
VERDE = (0,255,0)
BRANCO = (255,255,255)
VERDE_ESCURO = (10,50,10)

# =========================
# Fontes
# =========================
# Crie:
# - uma fonte principal (tamanho maior)
# - uma fonte menor (para mensagens)
fonte = pygame.font.Font("AttackGraffiti.ttf", 32)
fonte_continue = pygame.font.Font("AttackGraffiti.ttf", 24)

# =========================
# Textos
# =========================
# Crie os textos iniciais:
# - Score
# - Lives
# - Título do jogo
# - GAME OVER
# - Texto de continuar
#
# Use:
# fonte.render()
# get_rect()

pontuacao_texto = fonte.render(f"Score: {pontuacao}", True, VERDE)
pontuacao_rect = pontuacao_texto.get_rect()
pontuacao_rect.topleft = (10,10)

titulo_texto = fonte.render("Feed the Dragon", True, VERDE)
titulo_rect = titulo_texto.get_rect()
titulo_rect.centerx = comprimento//2
titulo_rect.y = 10

vidas_texto = fonte.render(f"Lives: {vidas_atuais}", True, VERDE)
vidas_rect = vidas_texto.get_rect()
vidas_rect.topright = (comprimento - 10, 10)

game_over_texto = fonte.render("GAME OVER", True, VERDE)
game_over_rect = game_over_texto.get_rect()
game_over_rect.center = (comprimento//2, largura//2)

continue_texto = fonte_continue.render("Pressione qualquer tecla para jogar novamente", True, VERDE)
continue_rect = continue_texto.get_rect()
continue_rect.center = (comprimento//2, largura//2 + 32)


# =========================
# Sons
# =========================
# Carregue:
# - som de moeda (colisão)
# - som de erro (quando perde vida)
# - música de fundo
#
# Dica:
# pygame.mixer.Sound()
# pygame.mixer.music.load()

som_moeda = pygame.mixer.Sound("coin_sound.wav")
som_perda = pygame.mixer.Sound("miss_sound.wav")
som_perda.set_volume(0.1)
pygame.mixer.music.load("ftd_background_music.wav")


# =========================
# Imagens
# =========================
# Carregue:
# - imagem do jogador (dragão)
# - imagem da moeda
#
# Crie os rects:
# - rect do jogador
# - rect da moeda

dragao = pygame.image.load("dragon_right.png")
dragao_rect = dragao.get_rect()
dragao_rect.left = 32
dragao_rect.centery = largura//2

moeda = pygame.image.load("coin.png")
moeda_rect = moeda.get_rect()
moeda_rect.x = comprimento + buffer
moeda_rect.y = random.randint(64, largura - 32)


# =========================
# Inicialização
# =========================
# Defina:
# - posição inicial do jogador (lado esquerdo, centro vertical)
# - posição inicial da moeda (fora da tela, à direita)
#
# Inicie a música com:
# pygame.mixer.music.play(-1)

pygame.mixer.music.play(-1)

# =========================
# Loop principal
# =========================
rodando = True
while rodando:

    # =========================
    # Eventos
    # =========================
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Aqui você pode implementar:
        # - pressionar tecla para reiniciar após game over


    # =========================
    # Movimento do jogador
    # =========================
    # Use:
    # pygame.key.get_pressed()
    #
    # Permita:
    # - mover para cima (W ou seta ↑)
    # - mover para baixo (S ou seta ↓)
    #
    # Limite o movimento:
    # - não sair do topo (ex: > 64)
    # - não sair da parte de baixo da tela

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and dragao_rect.top > 64:
        dragao_rect. y -= velocidade_jogador
    if keys[pygame.K_DOWN] and dragao_rect.bottom < largura:
        dragao_rect. y += velocidade_jogador

    # =========================
    # Movimento da moeda
    # =========================
    # Se a moeda sair da tela (x < 0):
    # - diminuir vidas
    # - tocar som de erro
    # - reposicionar moeda:
    #     x = largura + buffer
    #     y = valor aleatório
    #
    # Caso contrário:
    # - mover moeda para esquerda (diminuir x)

    if moeda_rect.x < 0:

        vidas_atuais -= 1
        som_perda.play()
        moeda_rect.x = comprimento + buffer
        moeda_rect.y = random.randint(64, largura - 32)
    else: 
        moeda_rect.x -= velocidade_atual_moeda


    # =========================
    # Colisão
    # =========================
    # Use:
    # rect_jogador.colliderect(rect_moeda)
    #
    # Se houver colisão:
    # - aumentar pontuação
    # - tocar som de moeda
    # - aumentar velocidade da moeda
    # - reposicionar moeda

    if dragao_rect.colliderect(moeda_rect):
        pontuacao += 1
        som_moeda.play()
        velocidade_atual_moeda += aceleracao
        moeda_rect.x = comprimento + buffer
        moeda_rect.y = random.randint(64, largura - 32)

    # =========================
    # Atualizar HUD
    # =========================
    # Atualize os textos:
    # - Score
    # - Lives
    #
    # Dica:
    # recriar com fonte.render()

    pontuacao_texto = fonte.render(f"Score: {pontuacao}", True, VERDE)
    vidas_texto = fonte.render(f"Lives: {vidas_atuais}", True, VERDE)


    # =========================
    # Game Over
    # =========================
    # Se vidas == 0:
    # - mostrar texto "GAME OVER"
    # - mostrar texto de continuar
    # - parar música

    if vidas_atuais ==0:
        tela.blit(game_over_texto, game_over_rect)
        tela.blit(continue_texto, continue_rect)
        pygame.mixer.music.stop()
        pygame.display.update()
    
    # Criar um loop de pausa:
    # while pausado:
    #     esperar tecla pressionada
    #     resetar:
    #         pontuação
    #         vidas
    #         posição jogador
    #         velocidade moeda
    #     reiniciar música

        pausado = True
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    vidas_atuais = vidas_iniciais
                    dragao_rect.y = largura//2
                    velocidade_atual_moeda = velocidade_inicial_moeda
                    pygame.mixer.music.play(-1)
                    pausado = False
                if event.type == pygame.QUIT:
                    pausado = False
                    rodando = False



    # =========================
    # Renderização
    # =========================
    # Limpar tela com fill()
     
    tela.fill(PRETO)
    # Desenhar:
    # - Score
    # - Lives
    # - título
    # - linha horizontal (HUD)

    tela.blit(pontuacao_texto, pontuacao_rect)
    tela.blit(titulo_texto, titulo_rect)
    tela.blit(vidas_texto, vidas_rect)
    pygame.draw.line(tela, BRANCO, (0,64), (comprimento, 64),2)

    # Desenhar personagens:
    # - jogador
    # - moeda
    tela.blit(dragao, dragao_rect)
    tela.blit(moeda, moeda_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()