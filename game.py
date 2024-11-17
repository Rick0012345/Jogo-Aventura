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
        while True:
            self.tela.fill(Cores.preto)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            

        
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()