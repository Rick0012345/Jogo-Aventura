import pygame




class Trex(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []

        for sprite in range(19):
            self.sprites.append(pygame.image.load(f'sprites/trex/{sprite}.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        

        self.rect = self.image.get_rect()
        self.rect.topleft = 1000, 550
        
    def update(self):
        self.atual = (self.atual + 0.2)
        if self.atual >= len(self.sprites):
            self.atual = 0 
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (177, 192))
        

class Soldado(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        
        for sprite in range(50):
            self.sprites.append(pygame.image.load(f'sprites/soldado/{sprite}.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (100, 750)

    
    def update(self):
    # Salva a posição atual do canto inferior esquerdo
        bottomleft = self.rect.bottomleft
        
        # Atualiza a animação
        self.atual = (self.atual + 0.2)
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (177, 192))
        
        # Reaplica a posição do canto inferior esquerdo
        self.rect = self.image.get_rect()
        self.rect.bottomleft = bottomleft

        