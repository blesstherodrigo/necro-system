from classes.personagens.jogador import Jogador
from game.menus import mostrar_menu, mostrar_status, mostrar_mochila
from game.exploracao import explorar


class Game:
    def __init__(self):
        self.jogador = None
        self.rodando = True

    def iniciar(self):
        self.criar_jogador()

        while self.rodando:
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

    def criar_jogador(self):
        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 5)