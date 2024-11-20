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
        self.fonte = pygame.font.Font(None, 74)  # Fonte para a mensagem de fim de jogo
        self.fim_de_jogo = False  # Controle de fim de jogo

    def run(self):
        todas_as_sprites = pygame.sprite.Group()
        trex = Trex()
        soldado = Soldado()
        todas_as_sprites.add(trex)
        todas_as_sprites.add(soldado)

        self.relogio = pygame.time.Clock()
        background = pygame.image.load('imgs/background.png').convert()
        background = pygame.transform.scale(background, (self.largura_tela, self.altura_tela))

        while True:
            self.tela.fill(Cores.preto)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN and not self.fim_de_jogo:
                    if event.key == K_LEFT:
                        soldado.mover_esquerda()
                    elif event.key == K_RIGHT:
                        soldado.mover_direita()
                    elif event.key == K_SPACE:
                        soldado.pular()
                if event.type == KEYUP:
                    if event.key in (K_LEFT, K_RIGHT):
                        soldado.parar()

            if not self.fim_de_jogo:
                # Verifica colisão entre soldado e trex
                if soldado.rect.colliderect(trex.rect):
                    self.fim_de_jogo = True

                todas_as_sprites.update()

            self.tela.blit(background, (0, 0))
            todas_as_sprites.draw(self.tela)

            if self.fim_de_jogo:
                # Exibe a mensagem de fim de jogo
                texto = self.fonte.render("Fim de Jogo!", True, Cores.branco)
                texto_rect = texto.get_rect(center=(self.largura_tela // 2, self.altura_tela // 2))
                self.tela.blit(texto, texto_rect)

            self.relogio.tick(60)
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
