import pygame

# --- CONFIGURAÇÃO INICIAL ---
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

# 1. Criando a Surface para a Zona Transparente (FORA DO LOOP)
raio = 150
# Criamos uma superfície do tamanho do círculo (diâmetro x diâmetro)
# O SRCALPHA permite que a cor tenha o quarto valor (Alpha/Transparência)
surface_transparente = pygame.Surface((raio * 2, raio * 2), pygame.SRCALPHA)

# 2. Desenhando o círculo na Surface auxiliar
# Cor: (R, G, B, Alpha) -> 100 é o nível de transparência (0 a 255)
cor_zona = (100, 100, 100, 100) 
pygame.draw.circle(surface_transparente, cor_zona, (raio, raio), raio)

# Configuração do Player
player_rect = pygame.Rect(100, 100, 30, 30)
centro_zona = pygame.Vector2(LARGURA // 2, ALTURA // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # Movimento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5
    if keys[pygame.K_UP]:    player_rect.y -= 5
    if keys[pygame.K_DOWN]:  player_rect.y += 5

    # Lógica de Colisão Circular (Distância entre centros)
    pos_player = pygame.Vector2(player_rect.center)
    distancia = pos_player.distance_to(centro_zona)
    
    colidindo = distancia < raio

    # --- DESENHO ---
    tela.fill((30, 30, 46)) # Fundo escuro

    # 3. Desenhando a Zona na tela (DENTRO DO LOOP)
    # Posicionamos a Surface para que o centro do círculo coincida com centro_zona
    tela.blit(surface_transparente, (centro_zona.x - raio, centro_zona.y - raio))

    # Desenha o Player (muda de cor se colidir)
    cor_p = (255, 0, 0) if colidindo else (0, 0, 255)
    pygame.draw.rect(tela, cor_p, player_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
