import pygame
import random

pygame.init()

# =========================
# Criação da tela
# =========================
# Defina o tamanho da tela e crie a janela do jogo

comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))
pygame.display.set_caption("Pegue o Pago")


# =================================
# Estabelecer as fontes para o jogo
# ==================================
# No jogo utilizamos duas fontes distintas:
# 1 - Tela inicial e Game Over
# 2 - Placar de pontuação

titulo = pygame.font.Font("titulo.ttf", 30 )
placar = pygame.font.Font("placar.ttf", 30)


# =========================
# Cores do jogo
# =========================
# Defina as cores que serão utilizadas (ex: PRETO, BRANCO, AZUL...)

PRETO = (0,0,0)

# =========================
# Imagens do jogo
# =========================
# No jogo iremos utilizar 5 imagens:
# 1 - Background
# 2 - Jacaré
# 3 - Pato
# 4 - Coração cheio
# 5 - Coração vazio

background = pygame.image.load("background.png")
pato = pygame.image.load("duck.png")
pato = pygame.transform.scale(pato, (30,30))

coracao_cheio = pygame.image.load("heart_full.png")
coracao_vazio = pygame.image.load("heart_empty.png")
coracao_cheio = pygame.transform.scale(coracao_cheio, (30,30))
coracao_vazio = pygame.transform.scale(coracao_vazio, (30,30))

jacare_direita = pygame.image.load("crocodile.png")
jacare_esquerda = pygame.transform.flip(jacare_direita, True, False)

jacare = jacare_direita
jacare = pygame.transform.scale(jacare, (30,30))

# =========================
# Sons do jogo
# =========================
# Iremos utilizar 3 sons distintos:
# 1 - Som de captura (colisão entre jacaré e pato)
# 2 - Música de fundo
# 3 - Som de fuga do pato

captura = pygame.mixer.Sound("sound_1.wav")
captura.set_volume(0.1)
fuga = pygame.mixer.Sound("sound_2.wav")
fuga.set_volume(0.1)
pygame.mixer.music.load("music.wav")
pygame.mixer.music.set_volume(0.1)

# =========================
# Clock
# =========================
# O FPS de 60 já garante uma fluidez boa para o jogo
FPS = 60
clock = pygame.time.Clock()


# =========================
# Estados 
# =========================
# No jogo teremos 3 estados:
# 1 - TELA_INICIAL
# 2 - JOGANDO
# 3 - GAME_OVER
# Eles devem ser controlados com o uso de uma variável
TELA_INICIAL = 0
JOGANDO = 1
GAME_OVER = 2

estado = TELA_INICIAL

# =========================
# Variáveis iniciais
# =========================
# São as variáveis que armazenam os valores do jogo:
# Exemplo: velocidade, placar e vidas
VELOCIDADE = 5
pontuacao = 0
VIDAS_MAX = 3
vidas = VIDAS_MAX

# Timer (3 segundos)
# Esse timer controla o tempo para o pato mudar sozinho
tempo_limite = 3000 # 3000ms -> 3s
tempo_inicio = pygame.time.get_ticks()

jacare_rect = jacare.get_rect()
pato_rect = pato.get_rect()

# As funções abaixo controlam algumas mecânicas do jogo.
# Elas já estão prontas, basta chamá-las quando necessário

def reposicionar_pato():
    pato_rect.x = random.randint(0, comprimento - 32)
    pato_rect.y = random.randint(60, largura - 32)


def resetar_jogo():
    global pontuacao, vidas, tempo_inicio
    pontuacao = 0
    vidas = VIDAS_MAX
    tempo_inicio = pygame.time.get_ticks()
    jacare_rect.center = (400, 300)
    pygame.mixer.music.play(-1)
    reposicionar_pato()


# =========================
# Inicialização
# =========================
# Aqui você deve:
# - Definir posição inicial do jacaré
# - Definir posição inicial do pato
reposicionar_pato()
jacare_rect.center = (400,300)


# =========================
# Loop principal
# =========================
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Aqui você pode implementar:
        # - ENTER para iniciar o jogo
        # - Qualquer tecla para reiniciar após Game Over

        if evento.type == pygame.KEYDOWN:
            if estado == TELA_INICIAL:
                if evento.key == pygame.K_RETURN:
                    estado = JOGANDO
                    resetar_jogo()
            elif estado == GAME_OVER:
                estado = JOGANDO
                resetar_jogo()

    # =========================
    # JOGANDO
    # =========================
    if estado == JOGANDO:

        # Movimento
        # Para os movimentos, utilize:
        # pygame.key.get_pressed()
        # e implemente:
        # - movimento contínuo
        # - limites da tela
        keys = pygame.key.get_pressed()
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

        if jacare_rect.left < 0:
            jacare_rect.left = 0
        if jacare_rect.right > comprimento:
            jacare_rect.right = comprimento
        if jacare_rect.top < 60:
            jacare_rect.top = 60
        if jacare_rect.bottom > largura:
            jacare_rect.bottom = largura

        # Tempo - controla a mudança automática do pato
        tempo_atual = pygame.time.get_ticks()
        tempo_passado = tempo_atual - tempo_inicio

        # Perde vida se passar de 3 segundos
        if tempo_passado >= tempo_limite:
            vidas -= 1
            fuga.play()
            reposicionar_pato()
            tempo_inicio = pygame.time.get_ticks()


        # =========================
        # Colisão
        # =========================
        # Implemente a lógica de colisão entre jacaré e pato
        # Dica: use colliderect()
        # Se houver colisão:
        # - aumenta o placar
        # - toca o som
        # - reposiciona o pato
        # - reseta o tempo
        if jacare_rect.colliderect(pato_rect):
            pontuacao += 1
            captura.play()
            reposicionar_pato()
            tempo_inicio = pygame.time.get_ticks()

        # =========================
        # Game Over
        # =========================
        # Se vidas <= 0:
        # - mudar o estado para GAME_OVER
        
        if vidas <= 0:
            estado = GAME_OVER

        # =========================
        # Renderizações iniciais
        # =========================
        # Aqui você deve desenhar:
        # - background
        # - barra superior (opcional)
        # - texto de pontuação
        
        tela.blit(background, (0,0))

        texto = placar.render(f"Pontução: {pontuacao}", True, PRETO)
        tela.blit(texto, (20,20))

        # ❤️ Corações (cheio/vazio)
        # Use um loop for para desenhar os corações:
        # Exemplo:
        # for i in range(VIDAS_MAX):
        #     if i < vidas:
        #         desenha coração cheio
        #     else:
        #         desenha coração vazio

        espaco = 35
        margem_direita = 10
        for i in range(VIDAS_MAX):
            x = comprimento - margem_direita - (i + 1) * espaco
            if i < vidas:
                tela.blit(coracao_cheio, (x,20))
            else:
                tela.blit(coracao_vazio, (x,20))


        # =========================
        # Personagens
        # =========================
        # Faça o blit do jacaré e do pato
        tela.blit(jacare, jacare_rect)
        tela.blit(pato, pato_rect)


    # =========================
    # TELA INICIAL
    # =========================
    elif estado == TELA_INICIAL:
        # Aqui deve ser implementada a tela inicial
        # Utilize:
        # - background
        # - texto "Pressione ENTER para iniciar"
        tela.blit(background, (0,0))
        texto = titulo.render("Pressione ENTER para iniciar", True, PRETO)
        texto_rect = texto.get_rect()
        texto_rect.center = (comprimento//2, largura//2)
        tela.blit(texto, texto_rect)
        pygame.mixer.music.stop()

    # =========================
    # GAME OVER
    # =========================
    elif estado == GAME_OVER:
        # Aqui deve ser implementada a tela de Game Over
        # Utilize:
        # - background
        # - texto "GAME OVER"
        # - texto "Pressione qualquer tecla para reiniciar"
        tela.blit(background, (0,0))
        texto = titulo.render("GAMER OVER", True, PRETO)
        texto_rect = texto.get_rect()
        texto_rect.center = (comprimento//2, largura//2)
        tela.blit(texto, texto_rect)

        texto2 = titulo.render("Pressione qualquer tecla", True, PRETO)
        texto_rect2 = texto2.get_rect()
        texto_rect2.center = (comprimento//2, largura//2 + 70)
        tela.blit(texto2, texto_rect2)
        pygame.mixer.music.stop()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()