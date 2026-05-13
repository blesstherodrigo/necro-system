# classes/jogo.py
from classes.personagens.jogador import Jogador
from data.fases import fase_1, fase_2, fase_3, fase_4
from game.menus import (
    mostrar_menu,
    mostrar_status,
    mostrar_mochila,
    mostrar_combate,
    limpar_tela,
    enter_continuar
)

class Jogo:
    def __init__(self):
        self.jogador = None
        self.inimigo = None
        self.rodando = True
        self.fases = [fase_1, fase_2, fase_3, fase_4]
        self.fase_atual = 0

    def criar_jogador(self):
        # aqui deve mostrar a imagem dos personagens, Homem e Mulher

        while True:
            print("[1] Homem | [2] Mulher")
            escolher_personagem = input("> ")
            
            limpar_tela()

            if escolher_personagem == "1":
                imagem = "Homem"
                break
            elif escolher_personagem == "2":
                imagem = "Mulher"
                break
            else:
                print("Opção inválida.")

        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 50, imagem)

    # criar combates para tipos diferentes de inimigos (zumbi comum e boss)
    def combate(self, inimigo):
        while self.jogador.esta_vivo() and inimigo.esta_vivo():
            limpar_tela()

            mostrar_combate(
                inimigo.nome,
                inimigo.vida,
                inimigo.vida_max,
                self.jogador.vida,
                self.jogador.vida_max
            )
            escolha = input("> ")

            if escolha == "1":
                self.jogador.atacar(inimigo)

                if inimigo.esta_vivo():
                    inimigo.atacar(self.jogador)

                enter_continuar()

            elif escolha == "2":
                print("\nVocê recuou.")
                enter_continuar()
                
                return "fugiu"

            else:
                print("Opção inválida.")
                enter_continuar()

        if self.jogador.esta_vivo():
            print(f"\nVocê derrotou {inimigo.nome}!")
            enter_continuar()
            
            return "venceu"
        
        print("\nVocê morreu.")
        enter_continuar()
        
        return "morreu"

    def explorar_fases(self):
        limpar_tela()

        if self.fase_atual >= len(self.fases):
            print("\nVocê já concluiu todas as fases disponíveis!")
            return "finalizado"

        fase = self.fases[self.fase_atual]

        print(f"=== FASE {fase['numero']}: {fase['nome'].upper()} ===")
        print(fase["descricao"])
        enter_continuar()

        for buscar_inimigo in fase["inimigos"]:
            limpar_tela()
            
            print(f"Um {buscar_inimigo.nome} apareceu!")
            enter_continuar()

            # criar combates para tipos diferentes de inimigos (zumbi comum e boss)
            resultado_do_combate = self.combate(buscar_inimigo)

            if resultado_do_combate == "morreu":
                return "morreu"

            if resultado_do_combate == "fugiu":
                return "fugiu"

        limpar_tela()
        print(f"Você concluiu a Fase {fase['numero']}: {fase['nome']}!")
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            print("\nParabéns! Você sobreviveu a todas as fases do NecroSystem!")
            return "finalizado"

        print("\nUma nova área foi desbloqueada.")
        return "venceu"

    def iniciar(self):
        # >Introdução do jogo AQUI<

        limpar_tela()
        self.criar_jogador()

        while self.rodando:
            mostrar_menu(
                self.jogador.nome,
                self.jogador.vida,
                self.jogador.vida_max,
                self.jogador.dano,
                self.fase_atual,
                len(self.fases)
            )
            escolha = input("> ")

            if escolha == "1":
                resultado = self.explorar_fases()

                if resultado == "morreu":
                    self.rodando = False

            elif escolha == "2":
                mostrar_status(self.jogador)    # mudar parametros

            elif escolha == "3":
                mostrar_mochila()

            elif escolha == "4":
                limpar_tela()
                print("Saindo do jogo...")
                self.rodando = False

            else:
                print("Opção inválida.")
                enter_continuar()


"""
código antigo:

# classes/jogo.py
from classes.personagens.jogador import Jogador
from game.menus import (
    mostrar_menu,
    mostrar_status,
    mostrar_mochila,
    limpar_tela,
    pausar
)

class Jogo:
    def __init__(self, fases):
        self.jogador = None
        self.rodando = True
        self.fases = fases
        self.fase_atual = 0

    def criar_jogador(self):
        # aqui deve mostrar a imagem dos personagens Homem e Mulher
        print("[1] Homem | [2] Mulher")
        personagem = input("> ")

        # >fazer um loop(while) caso o jogador escolher errado<
        if personagem == "1":
            imagem = "Homem"
        elif personagem == "2":
            imagem = "Mulher"
        else:
            # por enquanto, ao escolher errado fica Homem como padrão
            print("Opção inválida. Personagem definido como Homem por padrão.")
            imagem = "Homem"

        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 50, imagem)

    def criar_fases(self, vetor_fases):
        self.fases = vetor_fases
        return self.fases

    def combate(self, jogador, inimigo):
        while jogador.esta_vivo() and inimigo.esta_vivo():
            limpar_tela()

            print(f"=== COMBATE CONTRA {inimigo.nome.upper()} ===")
            print()
            print(f"Sua vida: {jogador.vida}/{jogador.vida_max}")
            print(f"Vida de {inimigo.nome}: {inimigo.vida}/{inimigo.vida_max}")
            print("-" * 30)
            print("1. Atacar")
            print("2. Fugir")
            print("-" * 30)

            escolha = input("> ")

            if escolha == "1":
                jogador.atacar(inimigo)

                if inimigo.esta_vivo():
                    inimigo.atacar(jogador)

                pausar()

            elif escolha == "2":
                print("\nVocê recuou. A fase continuará daqui quando explorar novamente.")
                return "fugiu"

            else:
                print("Opção inválida.")
                pausar()

        if jogador.esta_vivo():
            print(f"\nVocê derrotou {inimigo.nome}!")
            pausar()
            return "venceu"
        
        print("\nVocê morreu.")
        pausar()
        return "morreu"

    def explorar_fases(self, jogador):
        limpar_tela()

        if self.fase_atual >= len(self.fases):
            print("\nVocê já concluiu todas as fases disponíveis!")
            return "finalizado"

        fase = self.fases[self.fase_atual]

        print(f"=== FASE {fase['numero']}: {fase['nome'].upper()} ===")
        print(fase["descricao"])
        pausar()

        for inimigo in fase["inimigos"]:
            limpar_tela()
            print(f"Um {inimigo.nome} apareceu!")
            pausar()

            resultado_do_combate = self.combate(jogador, inimigo)

            if resultado_do_combate == "morreu":
                return "morreu"

            if resultado_do_combate == "fugiu":
                return "fugiu"

        limpar_tela()
        print(f"Você concluiu a Fase {fase['numero']}: {fase['nome']}!")
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            print("\nParabéns! Você sobreviveu a todas as fases do NecroSystem!")
            return "finalizado"

        print("\nUma nova área foi desbloqueada.")
        return "venceu"

    def iniciar(self):
        # >Introdução do jogo AQUI<

        limpar_tela()
        self.criar_jogador()

        while self.rodando:
            mostrar_menu(
                self.jogador,
                self.fase_atual,
                len(self.fases)
            )

            escolha = input("> ")

            if escolha == "1":
                resultado = self.explorar_fases(self.jogador)

                if resultado == "morreu":
                    self.rodando = False
                else:
                    pausar()    # para que serve este else???

            elif escolha == "2":
                mostrar_status(self.jogador)

            elif escolha == "3":
                mostrar_mochila()

            elif escolha == "4":
                limpar_tela()
                print("Saindo do jogo...")
                self.rodando = False

            else:
                print("Opção inválida.")
                pausar()


"""