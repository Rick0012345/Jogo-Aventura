import pygame
from pygame.locals import *
from sys import exit
from cores import Cores
from sprites import Trex, Soldado
class Game:
    def __init__(self):
        pygame.init()
        info_monitor = pygame.display.Info()
        self.largura_tela = info_monitor.current_w
        self.altura_tela = info_monitor.current_h
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Jogo de Aventura")
    


    def run(self):
        todas_as_sprites = pygame.sprite.Group()
        trex = Trex()
        soldado = Soldado()
        todas_as_sprites.add(trex)
        todas_as_sprites.add(soldado)

        self.relogio = pygame.time.Clock()
        background = pygame.image.load('imgs/background.png').convert()
        background = pygame.transform.scale(background,(self.largura_tela,self.altura_tela))

        while True:
            
              # Limita a taxa de atualização de 60 frames por segundo 
            self.tela.fill(Cores.preto)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            
            self.tela.blit(background,(0,0))
            todas_as_sprites.draw(self.tela)
            todas_as_sprites.update()
            
            self.relogio.tick(60)
            pygame.display.flip()
            

if __name__ == "__main__":
    game = Game()
    game.run()