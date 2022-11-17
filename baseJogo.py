import pygame as pg
from pygame.locals import(
    K_SPACE, K_ESCAPE, KEYDOWN, QUIT
)

import player

LARG = 400
ALTU = 400

preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
azul = (0,0,255)

pg.init()
tela = pg.display.set_mode((LARG, ALTU))
pg.display.set_caption("Jogo base Vesp")

jogador = player.Player(LARG,ALTU)

clock = pg.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    tela.fill(preto)
    teclas = pg.key.get_pressed()

    jogador.update(teclas)

    tela.blit(jogador.surf, jogador.rect)

    pg.display.flip()