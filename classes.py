import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk, ImageSequence
import random
from tkinter import messagebox

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.attack_power = random.randint(10, 20)

    def attack(self, opponent):
        damage = random.randint(5, self.attack_power)
        opponent.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health
        self.attack_power = random.randint(5, 15)

    def attack(self, player):
        damage = random.randint(3, self.attack_power)
        player.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, root, player, monster):
        self.root = root
        self.player = player
        self.monster = monster
        
        self.root.title("Batalha de Monstros")
        
        # Configuração da grade
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(4, weight=1)
        
        # Informações do jogador no canto inferior esquerdo
        self.player_status = tk.Label(root, text=f"{self.player.name}: {self.player.health} de vida", font=("Helvetica", 14))
        self.player_status.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        
        # Informações do monstro no canto superior direito
        self.monster_status = tk.Label(root, text=f"{self.monster.name}: {self.monster.health} de vida", font=("Helvetica", 14))
        self.monster_status.grid(row=0, column=1)
        
        # Status da batalha
        self.status_label = tk.Label(root, text="A batalha começou!", font=("Helvetica", 12))
        self.status_label.grid(row=1, column=0)
        
        # Botões alinhados horizontalmente
        self.attack_button = tk.Button(root, text="Atacar", command=self.attack_monster, width=15, height=2)
        self.attack_button.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        
        self.flee_button = tk.Button(root, text="Fugir", command=self.flee, width=15, height=2)
        self.flee_button.grid(row=2, column=0, pady=5, padx=5, sticky="e")
    
    def attack_monster(self):
        if self.player.is_alive() and self.monster.is_alive():
            damage = self.player.attack(self.monster)
            self.status_label.config(text=f"{self.player.name} atacou {self.monster.name} e causou {damage} de dano!")
            self.update_status()
            if self.monster.is_alive():
                self.root.after(1000, self.monster_attack)
            else:
                messagebox.showinfo("Vitória", f"Você derrotou {self.monster.name}!")

    def monster_attack(self):
        if self.player.is_alive():
            damage = self.monster.attack(self.player)
            self.status_label.config(text=f"{self.monster.name} atacou {self.player.name} e causou {damage} de dano!")
            self.update_status()
            if not self.player.is_alive():
                messagebox.showinfo("Derrota", f"{self.player.name} foi derrotado. Fim de jogo.")

    def update_status(self):
        self.player_status.config(text=f"{self.player.name}: {self.player.health} de vida")
        self.monster_status.config(text=f"{self.monster.name}: {self.monster.health} de vida")
    
    def flee(self):
        messagebox.showinfo("Fuga", f"{self.player.name} fugiu da batalha!")
        self.root.quit()

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
        self.game_window.resizable(False, False)  # Impede a expansão da janela

        # Adicionar o GIF de fundo usando um Label
        self.label = CTkLabel(self.game_window,text="")
        self.label.grid(row=0, column=0, sticky="nsew", rowspan=2, columnspan=2)  # Preenche toda a tela

        # Redimensionar o GIF para o tamanho da janela com o filtro LANCZOS
        self.gif_path = "gifs/cenario_fase_1.gif"
        self.gif = Image.open(self.gif_path)
        self.frames = [ImageTk.PhotoImage(frame.resize((800, 500), Image.LANCZOS)) for frame in ImageSequence.Iterator(self.gif)]

        # Definir a primeira imagem do GIF no Label
        self.label.configure(image=self.frames[0])

        # Adicionar o GIF de fantasma abaixo do Label do monstro
        self.fantasma_label = CTkLabel(self.game_window,text="")  # Usando CTkLabel em vez de tk.Label
        self.fantasma_label.grid(row=1, column=1, pady=10,padx=10)  # Define a posição do Label
        
        # Carregar e redimensionar o GIF de fantasma com suporte a transparência
        self.fantasma_path = "gifs/fantasma.gif"
        self.fantasma_gif = Image.open(self.fantasma_path)
        self.fantasma_frames = []
        for frame in ImageSequence.Iterator(self.fantasma_gif):
            frame = frame.convert("RGBA")  # Converte para RGBA para preservar a transparência
            resized_frame = frame.resize((100, 100), Image.LANCZOS)
            self.fantasma_frames.append(ImageTk.PhotoImage(resized_frame))
        
        # Definir a primeira imagem do GIF de fantasma
        self.fantasma_label.configure(image=self.fantasma_frames[0])

        # Iniciar a classe do jogo
        self.game = Game(self.game_window, self.player, self.monster)

        # Iniciar o loop principal da interface
        self.game_window.after(60, self.update_gif, 0)  # Inicia a atualização do GIF
        
        self.game_window.mainloop()

    def update_gif(self, frame_index):
        # Atualiza o GIF de fundo a cada frame
        self.label.configure(image=self.frames[frame_index])
        # Atualiza o GIF do fantasma a cada frame
        self.fantasma_label.configure(image=self.fantasma_frames[frame_index % len(self.fantasma_frames)])
        
        # Calcular o próximo índice para o frame do fundo e do fantasma
        next_frame = (frame_index + 1) % len(self.frames)
        
        # Atualizar a imagem novamente após 60ms
        self.game_window.after(60, self.update_gif, next_frame)  # 60 ms de intervalo entre os frames


# Instanciar e iniciar o jogo
jogo = LoopJogo()