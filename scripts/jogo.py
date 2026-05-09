# scripts/jogo.py

from classes.personagens.jogador import Jogador
from scripts.menus import mostrar_menu, mostrar_status, mostrar_mochila
from scripts.exploracao import explorar

class Jogo:
    def __init__(self):
        self.jogador = None
        self.rodando = True
    
    def criar_jogador(self):
        # escolher genero do jogador ???
        
        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 50)

    def iniciar(self):
        self.criar_jogador()

        while self.rodando:
            # >Introdução do jogo AQUI<

            mostrar_menu()
            escolha = input("> ")

            if escolha == "1":
                resultado = explorar(self.jogador)
                if resultado == "morreu":
                    self.rodando = False
            
            elif escolha == "2":
                mostrar_status(self.jogador)
            
            elif escolha == "3":
                mostrar_mochila()
            
            elif escolha == "4":
                self.rodando = False
            
            else:
                print("Opção inválida.")
