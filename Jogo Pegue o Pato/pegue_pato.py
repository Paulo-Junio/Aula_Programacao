import pygame
import random

pygame.init()

# Tela
comprimento = 800
largura = 600
tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Pegue o Pato")

# Fonte
fonte = pygame.font.Font("placar.ttf", 30)
fonte2 = pygame.font.Font("titulo.ttf", 30)

# Cores
AZUL_ACINZENTADO = (106,137,167)
PRETO = (0,0,0)
BRANCO = (255,255,255)

# Imagens
background = pygame.image.load("background.png")
jacare_direita = pygame.image.load("crocodile.png")
jacare_esquerda = pygame.transform.flip(jacare_direita, True, False)

jacare = jacare_direita
jacare = pygame.transform.scale(jacare, (30, 30))
pato = pygame.image.load("duck.png")
pato = pygame.transform.scale(pato, (30, 30))

# ❤️ Corações
coracao_cheio = pygame.image.load("heart_full.png")
coracao_vazio = pygame.image.load("heart_empty.png")

coracao_cheio = pygame.transform.scale(coracao_cheio, (30, 30))
coracao_vazio = pygame.transform.scale(coracao_vazio, (30, 30))

# Som
som = pygame.mixer.Sound("sound_1.wav")
som.set_volume(0.1)
som_2 = pygame.mixer.Sound("sound_2.wav")
som_2.set_volume(0.1)
pygame.mixer.music.load("music.wav")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Estados
TELA_INICIAL = 0
JOGANDO = 1
GAME_OVER = 2

estado = TELA_INICIAL

# Variáveis
VELOCIDADE = 5
placar = 0
VIDAS_MAX = 3
vidas = VIDAS_MAX

# Timer (3 segundos)
tempo_limite = 3000
tempo_inicio = pygame.time.get_ticks()

# Rects
jacare_rect = jacare.get_rect()
pato_rect = pato.get_rect()

def reposicionar_pato():
    pato_rect.x = random.randint(0, comprimento - 32)
    pato_rect.y = random.randint(60, largura - 32)

def resetar_jogo():
    global placar, vidas, tempo_inicio
    placar = 0
    vidas = VIDAS_MAX
    tempo_inicio = pygame.time.get_ticks()
    jacare_rect.center = (400, 300)
    pygame.mixer.music.play(-1)
    reposicionar_pato()

# Inicialização
reposicionar_pato()
jacare_rect.center = (400, 300)

pygame.mixer.music.set_volume(0.1)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if estado == TELA_INICIAL:
                if evento.key == pygame.K_RETURN:
                    estado = JOGANDO
                    resetar_jogo()

            elif estado == GAME_OVER:
                estado = JOGANDO
                resetar_jogo()

    keys = pygame.key.get_pressed()

    # =========================
    # JOGANDO
    # =========================
    if estado == JOGANDO:
        # Movimento
        if keys[pygame.K_LEFT]:
            jacare_rect.x -= VELOCIDADE
            jacare = jacare_esquerda
        if keys[pygame.K_RIGHT]:
            jacare_rect.x += VELOCIDADE
            jacare = jacare_direita
        if keys[pygame.K_UP]:
            jacare_rect.y -= VELOCIDADE
        if keys[pygame.K_DOWN]:
            jacare_rect.y += VELOCIDADE

        # Limites
        if jacare_rect.left < 0:
            jacare_rect.left = 0
        if jacare_rect.right > comprimento:
            jacare_rect.right = comprimento
        if jacare_rect.top < 60:
            jacare_rect.top = 60
        if jacare_rect.bottom > largura:
            jacare_rect.bottom = largura

        # Tempo
        tempo_atual = pygame.time.get_ticks()
        tempo_passado = tempo_atual - tempo_inicio

        # Perde vida se passar de 3s
        if tempo_passado >= tempo_limite:
            vidas -= 1
            som_2.play()
            reposicionar_pato()
            tempo_inicio = pygame.time.get_ticks()

        # Colisão
        if jacare_rect.colliderect(pato_rect):
            placar += 1
            som.play()
            reposicionar_pato()
            tempo_inicio = pygame.time.get_ticks()

        # Game over
        if vidas <= 0:
            estado = GAME_OVER

        # Render
        tela.blit(background, (0,0))

        # Pontuação
        texto = fonte.render(f"Pontuação: {placar}", True, PRETO)
        tela.blit(texto, (20,20))

        # ❤️ Corações (cheio/vazio)
        espaco = 35
        margem_direita = 10

        for i in range(VIDAS_MAX):
            x = comprimento - margem_direita - (i + 1) * espaco

            if i < vidas:
                tela.blit(coracao_cheio, (x, 20))
            else:
                tela.blit(coracao_vazio, (x, 20))

        # Personagens
        tela.blit(jacare, jacare_rect)
        tela.blit(pato, pato_rect)

    # =========================
    # TELA INICIAL
    # =========================
    elif estado == TELA_INICIAL:
        tela.blit(background, (0,0))

        texto = fonte2.render("Pressione ENTER para iniciar", True, PRETO)
        tela.blit(texto, texto.get_rect(center=(400,300)))
        pygame.mixer.music.stop()

    # =========================
    # GAME OVER
    # =========================
    elif estado == GAME_OVER:
        tela.blit(background, (0,0))

        texto1 = fonte2.render("GAME OVER", True, PRETO)
        texto2 = fonte2.render("Pressione qualquer tecla", True, PRETO)

        tela.blit(texto1, texto1.get_rect(center=(400,250)))
        tela.blit(texto2, texto2.get_rect(center=(400,320)))
        pygame.mixer.music.stop()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()