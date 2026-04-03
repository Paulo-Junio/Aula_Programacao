import pygame

pygame.init()

comprimento = 800
largura = 600

tela = pygame.display.set_mode((comprimento, largura))


vermelho = (255,0,0)
retangulo = pygame.draw.rect(tela, vermelho, [200, 200, 150, 100],5 )


rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    tela.fill((0,0,0))
    
    retangulo =pygame.draw.rect(tela, vermelho, [200, 200, 150, 100] )


    pygame.display.update()
pygame.quit()
