import pygame
import random as rd



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
        self.rect.x = 1000  # Começa na posição x inicial
        self.rect.y = 600  # Defina uma altura apropriada
        self.velocidade_x = 9  # Velocidade inicial do T-Rex no eixo x
        self.aceleracao = 0.005  # Fator de aceleração

    def update(self):
        self.atual = (self.atual + 0.2)
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (177, 192))

        # Atualiza a posição e aplica a aceleração
        self.rect.x += self.velocidade_x
        self.velocidade_x += self.aceleracao if self.velocidade_x > 0 else -self.aceleracao

        # Faz o T-Rex voltar ao outro lado se sair da tela
        if self.rect.right >= pygame.display.get_surface().get_width() or self.rect.left <= 0:
            self.velocidade_x = -self.velocidade_x

        

class Soldado(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        for sprite in range(1,9):
            self.sprites.append(pygame.image.load(f'sprites/soldado/{sprite}.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 770


        # Velocidade de movimento e estado do salto
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 1
        self.no_chao = True

    def update(self):
        # Salva a posição atual do canto inferior esquerdo
        bottomleft = self.rect.bottomleft

        # Atualiza a animação
        self.atual = (self.atual + 0.2)
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (100, 170))

        # Reaplica a posição do canto inferior esquerdo
        self.rect = self.image.get_rect()
        self.rect.bottomleft = bottomleft

        # Atualiza a posição horizontal
        self.rect.x += self.velocidade_x

        # Atualiza a posição vertical (pulo)
        if not self.no_chao:
            self.velocidade_y += self.gravidade
            self.rect.y += self.velocidade_y

        # Checa se está no chão
        if self.rect.bottom >= 770:  # Altura do chão
            self.rect.bottom = 770
            self.no_chao = True
            self.velocidade_y = 0

    def mover_esquerda(self):
        self.velocidade_x = -5

    def mover_direita(self):
        self.velocidade_x = 5

    def parar(self):
        self.velocidade_x = 0

    def pular(self):
        if self.no_chao:
            self.velocidade_y = -25  # Força do pulo
            self.no_chao = False
