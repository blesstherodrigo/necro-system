from classes.personagens.jogador import Jogador
from objetos.zumbis import zumbis

class Game:
    def __init__(self):
        self.jogador = None
        self.rodando = True

    def iniciar(self):
        self.criar_jogador()

        while self.rodando:
            self.mostrar_menu()
            escolha = input("> ")

            if escolha == "1":
                self.fase_hospital()
            elif escolha == "2":
                self.mostrar_status()
            elif escolha == "3":
                self.rodando = False
            else:
                print("Opção inválida.")

    def criar_jogador(self):
        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 5)

    def mostrar_menu(self):
        print("\n=== NECRO SYSTEM ===")
        print("1. Explorar")
        print("2. Status")
        print("3. Sair")

    def mostrar_status(self):
        print(f"\nNome: {self.jogador.nome}")
        print(f"Vida: {self.jogador.vida}/{self.jogador.vida_max}")
        print(f"Dano: {self.jogador.dano}")

    def fase_hospital(self):
        print("\nVocê começa a explorar...")
        print(f"Um {zumbis[0].nome} apareceu!")
        self.combate(zumbis[0])

    def combate(self, inimigo):
        print(f"\nCombate contra {inimigo.nome}!")

        while self.jogador.esta_vivo() and inimigo.esta_vivo():
            print(f"\nSua vida: {self.jogador.vida}/{self.jogador.vida_max}")
            print(f"Vida do {inimigo.nome}: {inimigo.vida}/{inimigo.vida_max}")

            print("\n1. Atacar")
            print("2. Fugir")
            escolha = input("> ")

            if escolha == "1":
                self.jogador.atacar(inimigo)

                if inimigo.esta_vivo():
                    inimigo.atacar(self.jogador) #

            elif escolha == "2":
                print("Você fugiu do combate.")
                return

            else:
                print("Opção inválida.")

        if self.jogador.esta_vivo():
            print(f"\nVocê derrotou {inimigo.nome}!")
        else:
            print("\nVocê morreu.")
            self.rodando = False
        
        print("O lugar ficou silencioso...")
        print('Apareceu outro zumbi.')
        
        self.combate(zumbis[1])
        
jogo = Game()
jogo.iniciar()