import pygame
import random

# =========================
# Inicialização
# =========================
pygame.init()

# Tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Placar Dinâmico")

# Clock
clock = pygame.time.Clock()

# =========================
# Cores
# =========================
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 200, 0)
PRETO = (0, 0, 0)

# =========================
# Fonte
# =========================
fonte = pygame.font.SysFont("Arial", 30)

# =========================
# Jogador (Rect)
# =========================
jogador = pygame.Rect(100, 100, 50, 50)
velocidade = 5

# =========================
# Item coletável (Rect)
# =========================
item = pygame.Rect(
    random.randint(0, LARGURA - 30),
    random.randint(50, ALTURA - 30),
    30,
    30
)

# =========================
# Pontuação
# =========================
pontuacao = 0

# =========================
# Loop principal
# =========================
rodando = True
while rodando:

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # =========================
    # Movimento do jogador
    # =========================
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # =========================
    # Limitar jogador na tela
    # =========================
    if jogador.left < 0:
        jogador.left = 0
    if jogador.right > LARGURA:
        jogador.right = LARGURA
    if jogador.top < 0:
        jogador.top = 0
    if jogador.bottom > ALTURA:
        jogador.bottom = ALTURA

    # =========================
    # Colisão (coleta do item)
    # =========================
    if jogador.colliderect(item):
        pontuacao += 10

        # Reposiciona o item aleatoriamente
        item.x = random.randint(0, LARGURA - item.width)
        item.y = random.randint(50, ALTURA - item.height)

    # =========================
    # Desenho na tela
    # =========================
    tela.fill(BRANCO)

    # Jogador
    pygame.draw.rect(tela, AZUL, jogador)

    # Item
    pygame.draw.rect(tela, VERDE, item)

    # =========================
    # Placar (texto dinâmico)
    # =========================
    texto_placar = fonte.render(f"Pontuação: {pontuacao}", True, PRETO)

    # Posicionamento com get_rect()
    rect_placar = texto_placar.get_rect()
    rect_placar.topright = (LARGURA - 10, 10)  # canto superior direito

    tela.blit(texto_placar, rect_placar)

    # =========================
    # Atualização da tela
    # =========================
    pygame.display.update()
    clock.tick(60)
pygame.quit()