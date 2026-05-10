# classes/jogo.py
from classes.personagens.jogador import Jogador
from game.menus import mostrar_menu, mostrar_status, mostrar_mochila

class Jogo:
    def __init__(self, fases):
        self.jogador = None
        self.rodando = True
        self.fases = fases
        self.fase_atual = 0

    def criar_jogador(self):
        print("[1] Homem | [2] Mulher")
        personagem = input("> ")

        if personagem == "1":
            imagem = "Homem"
        elif personagem == "2":
            imagem = "Mulher"
        else:
            print("Opção inválida. Personagem definido como Homem por padrão.")
            imagem = "Homem"

        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 50, imagem)

    def criar_fases(self, vetor_fases):
        self.fases = vetor_fases
        return self.fases

    def combate(self, jogador, inimigo):
        print(f"\nCombate contra {inimigo.nome}!")

        while jogador.esta_vivo() and inimigo.esta_vivo():
            print(f"\nSua vida: {jogador.vida}/{jogador.vida_max}")
            print(f"Vida de {inimigo.nome}: {inimigo.vida}/{inimigo.vida_max}")

            print("\n1. Atacar")
            print("2. Fugir")
            escolha = input("> ")

            if escolha == "1":
                jogador.atacar(inimigo)

                if inimigo.esta_vivo():
                    inimigo.atacar(jogador)

            elif escolha == "2":
                print("Você fugiu do combate.")
                return "fugiu"

            else:
                print("Opção inválida.")

        if jogador.esta_vivo():
            print(f"\nVocê derrotou {inimigo.nome}!")
            return "venceu"

        print("\nVocê morreu.")
        return "morreu"

    def explorar(self, jogador):
        if self.fase_atual >= len(self.fases):
            print("\nVocê já concluiu todas as fases disponíveis!")
            return "finalizado"

        fase = self.fases[self.fase_atual]

        print(f"\n=== FASE {fase['numero']}: {fase['nome'].upper()} ===")
        print(fase["descricao"])

        for inimigo in fase["inimigos"]:
            print(f"\nUm {inimigo.nome} apareceu!")
            resultado_do_combate = self.combate(jogador, inimigo)

            if resultado_do_combate == "morreu":
                return "morreu"

            if resultado_do_combate == "fugiu":
                print("\nVocê recuou. A fase continuará daqui quando explorar novamente.")
                return "fugiu"

        print(f"\nVocê concluiu a Fase {fase['numero']}: {fase['nome']}!")
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            print("\nParabéns! Você sobreviveu a todas as fases do NecroSystem!")
            return "finalizado"

        print("\nUma nova área foi desbloqueada.")
        return "venceu"

    def iniciar(self):
        # >Introdução do jogo AQUI<
        
        self.criar_jogador()

        while self.rodando:
            mostrar_menu()
            escolha = input("> ")

            if escolha == "1":
                resultado = self.explorar(self.jogador)

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