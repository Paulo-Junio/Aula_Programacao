import pygame

# --- CONFIGURAÇÃO INICIAL ---
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

# 1. Carregando a Imagem do Player (FORA DO LOOP)
player_image = pygame.image.load("assets/player.png").convert_alpha()
# Criamos o Rect a partir da imagem para controlar a posição
player_rect = player_image.get_rect(center=(100, 100))

# 2. Configuração da Zona Circular Transparente
raio_zona = 150
centro_zona = pygame.Vector2(LARGURA // 2, ALTURA // 2)

# Criando a Surface para a transparência
surface_zona = pygame.Surface((raio_zona * 2, raio_zona * 2), pygame.SRCALPHA)
# Cor com Alpha (R, G, B, Alpha)
pygame.draw.circle(surface_zona, (100, 100, 100, 100), (raio_zona, raio_zona), raio_zona)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # --- MOVIMENTO CONTÍNUO ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player_rect.x -= 5
    if keys[pygame.K_RIGHT]: player_rect.x += 5
    if keys[pygame.K_UP]:    player_rect.y -= 5
    if keys[pygame.K_DOWN]:  player_rect.y += 5

    # --- LÓGICA DE COLISÃO CIRCULAR (Imagem vs Círculo) ---
    # Pegamos o centro do Rect da imagem
    pos_player = pygame.Vector2(player_rect.center)
    # Calculamos a distância até o centro da zona
    distancia = pos_player.distance_to(centro_zona)
    
    # Se a distância for menor que o raio da zona, houve colisão!
    colidindo = distancia < raio_zona

    # --- DESENHO ---
    tela.fill((30, 30, 46))

    # Desenha a Zona Transparente
    tela.blit(surface_zona, (centro_zona.x - raio_zona, centro_zona.y - raio_zona))

    # Desenha a Imagem do Player usando o seu Rect
    tela.blit(player_image, player_rect)

    # Feedback visual de colisão (opcional: desenhar um contorno se colidir)
    if colidindo:
        pygame.draw.rect(tela, (255, 0, 0), player_rect, 2) # Desenha borda vermelha no Rect da imagem

    pygame.display.update()
    clock.tick(60)

pygame.quit()

