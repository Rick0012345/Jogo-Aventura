import pygame




class Trex(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/trex/0.png'))
        self.sprites.append(pygame.image.load('sprites/trex/1.png'))
        self.sprites.append(pygame.image.load('sprites/trex/2.png'))
        self.sprites.append(pygame.image.load('sprites/trex/3.png'))
        self.sprites.append(pygame.image.load('sprites/trex/4.png'))
        self.sprites.append(pygame.image.load('sprites/trex/5.png'))
        self.sprites.append(pygame.image.load('sprites/trex/6.png'))
        self.sprites.append(pygame.image.load('sprites/trex/7.png'))
        self.sprites.append(pygame.image.load('sprites/trex/8.png'))
        self.sprites.append(pygame.image.load('sprites/trex/9.png'))
        self.sprites.append(pygame.image.load('sprites/trex/10.png'))
        self.sprites.append(pygame.image.load('sprites/trex/11.png'))
        self.sprites.append(pygame.image.load('sprites/trex/12.png'))
        self.sprites.append(pygame.image.load('sprites/trex/13.png'))
        self.sprites.append(pygame.image.load('sprites/trex/14.png'))
        self.sprites.append(pygame.image.load('sprites/trex/15.png'))
        self.sprites.append(pygame.image.load('sprites/trex/16.png'))
        self.sprites.append(pygame.image.load('sprites/trex/17.png'))
        self.sprites.append(pygame.image.load('sprites/trex/18.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        


