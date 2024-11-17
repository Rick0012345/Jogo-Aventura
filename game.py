import pygame
from pygame.locals import *
from sys import exit
from cores import Cores
from sprites import Trex
class Game:
    def __init__(self):
        pygame.init()
        self.largura_tela = 800
        self.altura_tela = 600
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Jogo de Aventura")
    


    def run(self):
        todas_as_sprites = pygame.sprite.Group()
        trex = Trex()
        todas_as_sprites.add(trex)
        self.relogio = pygame.time.Clock()

    

        while True:
            
            self.relogio.tick(60)  # Limita a taxa de atualização de 60 frames por segundo 
            self.tela.fill(Cores.preto)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            

            todas_as_sprites.draw(self.tela)
            todas_as_sprites.update()
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()