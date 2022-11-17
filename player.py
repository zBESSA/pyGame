import pygame as pg
from pygame.locals import(
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT
)

# defino a classe de um jogador...

class Player(pg.sprite.Sprite):
    """
    Define a classe de um jogador (surface)
    """
    def __init__(self, largura, altura):
        super(Player,self).__init__()
        self.largura = largura
        self.altura = altura
        self.surf = pg.Surface((75,25))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect()

    def limite(self):
        # mantem a surface dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
            self.sentido = 'd'
        if self.rect.right > self.largura:
            self.rect.right = self.largura
            self.sentido = 'e'
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.altura:
            self.rect.bottom = self.altura        

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
          self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
        self.limite()
        
    def automov(self):
        if self.sentido == 'd':
            self.rect.move_ip(5,0)
        if self.sentido == 'e':
            self.rect.move_ip(-5,0)
        self.limite()    
            