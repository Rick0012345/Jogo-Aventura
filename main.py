import tkinter as tk
from tkinter import messagebox
import random

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
        self.monster_status.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        
        # Status da batalha
        self.status_label = tk.Label(root, text="A batalha começou!", font=("Helvetica", 12))
        self.status_label.grid(row=1, column=0, pady=10, padx=10)
        
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

# Criando o jogo
