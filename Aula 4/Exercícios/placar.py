# Atividade de Casa 2: Placar Dinâmico
# Objetivo: Praticar a atualização de texto na tela com base em interações e colisões, 
# reforçando o uso de Rects .

# 1. Crie um jogo simples onde um personagem (controlado pelo teclado) pode "coletar" 
# um item (outro retângulo ou imagem).

# 2. Implemente um placar no canto superior da tela que exiba a pontuação atual. A 
# pontuação deve começar em 0.

# 3. Cada vez que o personagem colidir com o item (você pode usar 
# pygame.Rect.colliderect() ), a pontuação deve aumentar em 10 pontos e o item deve 
# reaparecer em uma nova posição aleatória.

# 4. O texto do placar deve ser atualizado a cada coleta, sempre usando 
# get_rect() para  garantir o posicionamento correto e centralizado (ou alinhado à direita/esquerda) na sua área.