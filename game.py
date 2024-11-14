from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import random
from main import Player, Monster, Game

class TelaBoasVindas:
    def __init__(self):
        self.root = CTk()
        self.root.geometry("800x500")
        
        # Configurar weights para centralizar os elementos
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        
        # Carregar a imagem de fundo da TelaBoasVindas com CTkImage
        self.bg_image = Image.open("imgs/background.jpg")
        self.bg_image = CTkImage(self.bg_image, size=(800, 500))  # Converte para CTkImage
        
        # Criar um label para a imagem de fundo da TelaBoasVindas
        self.background_label = CTkLabel(self.root, image=self.bg_image)
        self.background_label.place(relwidth=1, relheight=1)
        
        # Adicionar widgets usando grid com padding menor
        self.label = CTkLabel(self.root, text="Bem-vindo à Batalha de Monstros! Insira seu nome:", font=("Helvetica", 20), bg_color='transparent', fg_color='#a67521', corner_radius=10)
        self.label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        
        self.entry_name = CTkEntry(self.root, font=("Helvetica", 12))
        self.entry_name.grid(row=1, column=0, columnspan=3, pady=5, padx=10)
        
        self.start_button = CTkButton(self.root, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10)
        
        self.root.mainloop()

    def iniciar_jogo(self):
        player_name = self.entry_name.get()
        if player_name.strip() == "":
            messagebox.showerror("Erro", "Nome não deve ser vazio! ")
            return
        
        # Fechar a tela de boas-vindas
        self.root.quit()
        
        # Criar a animação do GIF de fundo para a tela do jogo
        self.bg_image_game = Image.open("gifs/cenario_fase_1.gif")
        self.frames = []
        
        # Converter todos os frames para CTkImage e mantê-los em self.frames
        for frame in ImageSequence.Iterator(self.bg_image_game):
            frame = CTkImage(frame)  # Converte para CTkImage
            self.frames.append(frame)
        
        self.frame_index = 0
        
        # Criar a janela principal do jogo
        game_window = Tk()
        game_window.geometry("800x500")
        
        # Criar o label de fundo da janela do jogo
        self.background_label_game = Label(game_window, image=self.frames[self.frame_index])
        self.background_label_game.place(relwidth=1, relheight=1)
        
        # Iniciar a animação do GIF
        self.animate_gif(game_window)

        player = Player(name=player_name)
        monster = Monster(name="Monstro Selvagem")
        
        game = Game(game_window, player, monster)
        game_window.mainloop()

    def animate_gif(self, game_window):
        # Atualiza o fundo com o próximo frame do GIF
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.background_label_game.configure(image=self.frames[self.frame_index])
        game_window.after(60, self.animate_gif, game_window)  # Atualiza o GIF a cada 100ms


# Inicializa a tela de boas-vindas
Tela = TelaBoasVindas()
