import pygame

# --- FORA DO LOOP PRINCIPAL (Configurações e Assets) ---
pygame.init()

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Teste de Colisão")

# Clock para controlar o FPS
clock = pygame.time.Clock()
FPS = 60

# Cores
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
CINZA = (100, 100, 100)
BRANCO = (255, 255, 255)

# Partícula (Player)
velocidade = 5
cor_player = AZUL
player_rect = pygame.Rect(0, 0, 30, 30)
player_rect.center = (LARGURA // 2, ALTURA // 2)

# Zona de Perigo (Retângulo)
zona_rect = pygame.Rect(0, 0, 200, 200)
zona_rect.center = (LARGURA // 2, ALTURA // 2)

# Texto e Som
fonte = pygame.font.SysFont("Arial", 48)
som_alerta = pygame.mixer.Sound("assets/alert.wav") # Precisa do arquivo na pasta
tocando_som = False # Controle para não dar play() toda hora

running = True
while running:
    # --- DENTRO DO LOOP (Eventos) ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # --- DENTRO DO LOOP (Lógica de Movimento) ---
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        player_rect.x -= velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        player_rect.x += velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        player_rect.y -= velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        player_rect.y += velocidade

    # --- DENTRO DO LOOP (Limites de Tela) ---
    if player_rect.left < 0: player_rect.left = 0
    if player_rect.right > LARGURA: player_rect.right = LARGURA
    if player_rect.top < 0: player_rect.top = 0
    if player_rect.bottom > ALTURA: player_rect.bottom = ALTURA

    # --- DENTRO DO LOOP (Lógica de Colisão) ---
    if player_rect.colliderect(zona_rect):
        cor_player = VERMELHO
        texto = fonte.render("PERIGO!", True, BRANCO)
        if not tocando_som:
            som_alerta.play(-1) # Toca em loop
            tocando_som = True
    else:
        cor_player = AZUL
        texto = None
        if tocando_som:
            som_alerta.stop()
            tocando_som = False

    # --- DENTRO DO LOOP (Desenho) ---
    tela.fill((30, 30, 46)) # Fundo escuro
    
    pygame.draw.rect(tela, CINZA, zona_rect) # Desenha a zona
    pygame.draw.rect(tela, cor_player, player_rect) # Desenha o player
    
    if texto:
        # Centraliza o texto no topo
        pos_texto = texto.get_rect(center=(LARGURA//2, 50))
        tela.blit(texto, pos_texto)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
