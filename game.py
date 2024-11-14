import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Para carregar e exibir a imagem de fundo
from main import Player, Monster, Game

# Classe WelcomeScreen para a tela de boas-vindas
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
        
        # Carregar a imagem de fundo
        self.background_image = Image.open("imgs/background.jpg")
        self.background_image = self.background_image.resize((800, 500), Image.LANCZOS)  # Usando Image.LANCZOS
        self.bg_image_tk = ImageTk.PhotoImage(self.background_image)
        
        # Criar um label para a imagem de fundo
        self.background_label = CTkLabel(self.root, image=self.bg_image_tk)
        self.background_label.place(relwidth=1, relheight=1)
        
        # Adicionar widgets usando grid com padding menor
        self.label = CTkLabel(self.root, text="Bem-vindo à Batalha de Monstros! Insira seu nome:", font=("Helvetica", 20), bg_color='transparent',fg_color='#a67521', corner_radius=10)
        self.label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        
        self.entry_name = CTkEntry(self.root, font=("Helvetica", 12))
        self.entry_name.grid(row=1, column=0, columnspan=3, pady=5, padx=10)
        
        self.start_button = CTkButton(self.root, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.start_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10)
        
        self.root.mainloop()

    def iniciar_jogo(self):
        pass
        


# Inicializa a tela de boas-vindas
Tela = TelaBoasVindas()
