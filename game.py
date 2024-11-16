import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk, ImageSequence
from main import Player, Monster, Game

class LoopJogo:
    def __init__(self):
        # Obtenha o nome do jogador diretamente ou configure um nome padrão
        player_name = "Jogador"  # Pode ser alterado para entrada do usuário, se desejado

        # Criar um jogador e um monstro
        self.player = Player(name=player_name)
        self.monster = Monster(name="Monstro Selvagem")

        # Criar a janela principal do jogo
        self.game_window = CTk()
        self.game_window.geometry("800x500")

        # Adicionar o GIF de fundo usando um Label
        self.label = tk.Label(self.game_window)
        self.label.grid(row=0, column=0, sticky="nsew")  # Usando grid para preencher a tela

        # Redimensionar o GIF para o tamanho da janela com o filtro LANCZOS
        self.gif_path = "gifs/cenario_fase_1.gif"
        self.gif = Image.open(self.gif_path)
        self.frames = [ImageTk.PhotoImage(frame.resize((800, 500), Image.LANCZOS)) for frame in ImageSequence.Iterator(self.gif)]

        # Definir a primeira imagem do GIF no Label
        self.label.config(image=self.frames[0])

        # Função para atualizar o GIF na tela
        self.update_gif(0)

        # Iniciar a classe do jogo
        self.game = Game(self.game_window, self.player, self.monster)

        # Definir expansão do grid para preencher a tela
        self.game_window.grid_rowconfigure(0, weight=1)  # Permitindo que a linha de fundo se expanda
        self.game_window.grid_columnconfigure(0, weight=1)  # Permitindo que a coluna de fundo se expanda

        # Iniciar o loop principal da interface
        self.game_window.mainloop()

    def update_gif(self, frame_index):
        # Atualiza o GIF a cada frame
        self.label.config(image=self.frames[frame_index])
        next_frame = (frame_index + 1) % len(self.frames)
        self.game_window.after(60, self.update_gif, next_frame)  # 100 ms de intervalo entre os frames

# Instanciar e iniciar o jogo
jogo = LoopJogo()
