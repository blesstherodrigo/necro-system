# classes/jogo.py
from classes.personagens.jogador import Jogador
from data.fases import fase_1, fase_2, fase_3, fase_4
from game.textos import (
    limpar_tela,
    enter_continuar,
    opcao_invalida,
    mostrar_menu,
    mostrar_status,
    mostrar_mochila,
    confirmacao_sair_do_jogo,
    saindo_do_jogo,
    mostrar_combate,
    recuou_do_combate,
    introducao_fase
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

            if escolher_personagem == "1":
                imagem = "imgem do jogador homem aqui"
                break
            elif escolher_personagem == "2":
                imagem = "imagem do jogador mulher aqui"
                break
            else:
                opcao_invalida()

        limpar_tela()
        nome = input("Digite seu nome: ")
        self.jogador = Jogador(nome, 1000, 1000, 50, imagem)

    # criar combates para tipos diferentes de inimigos (zumbi comum e boss)
    def combate(self):
        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():
            opcao_combate_escolhida = mostrar_combate(
                self.inimigo.nome,
                self.inimigo.vida,
                self.inimigo.vida_max,
                self.jogador.vida,
                self.jogador.vida_max
            )

            if opcao_combate_escolhida == "1":
                limpar_tela()
                self.jogador.atacar(self.inimigo)

                if self.inimigo.esta_vivo():
                    self.inimigo.atacar(self.jogador)

                enter_continuar()

            elif opcao_combate_escolhida == "2":
                recuou_do_combate()
                return "fugiu"

            else:
                opcao_invalida()

        if self.jogador.esta_vivo():
            print(f"\nVocê derrotou {self.inimigo.nome}!")
            enter_continuar()
            
            return "venceu"
        
        print("\nVocê morreu.")
        enter_continuar()
        
        return "morreu"

    def buscar_fases(self):
        buscar_fase_atual = self.fases[self.fase_atual]
        return buscar_fase_atual

    def explorar_fases(self):
        if self.fase_atual >= len(self.fases):
            limpar_tela()
            print("\nVocê já concluiu todas as fases disponíveis!")
            enter_continuar()
            return "finalizado"

        jogar_fase = self.buscar_fases()

        introducao_fase(jogar_fase['numero'], jogar_fase['nome'], jogar_fase["descricao"])

        # fazer um metodo separado para buscar os inimigos de cada fase ????
        for buscar_inimigo in jogar_fase["inimigos"]:
            self.inimigo = buscar_inimigo

            limpar_tela()
            print(f"Um {self.inimigo.nome} apareceu!")
            enter_continuar()

            # criar combates para tipos diferentes de inimigos (zumbi comum e boss)
            resultado_do_combate = self.combate()

            if resultado_do_combate == "morreu":
                return "morreu"

            if resultado_do_combate == "fugiu":
                return "fugiu"

        limpar_tela()
        print(f"Você concluiu a Fase {jogar_fase['numero']}: {jogar_fase['nome']}!")
        enter_continuar()
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            print("Parabéns! Você sobreviveu ao NecroSystem!")
            enter_continuar()

        print("Uma nova área foi desbloqueada.")
        enter_continuar()
        return "venceu"

    def iniciar(self):
        # >Introdução do jogo AQUI<

        self.criar_jogador()

        while self.rodando:
            opcao_menu_escolhida = mostrar_menu(
                self.jogador.nome,
                self.jogador.vida,
                self.jogador.vida_max,
                self.jogador.dano,
                self.fase_atual,
                len(self.fases)
            )

            if opcao_menu_escolhida == "1":
                resultado = self.explorar_fases()

                if resultado == "morreu":
                    self.rodando = False

            elif opcao_menu_escolhida == "2":
                mostrar_status(
                    self.jogador.nome,
                    self.jogador.vida,
                    self.jogador.vida_max,
                    self.jogador.dano
                )

            elif opcao_menu_escolhida == "3":
                mostrar_mochila()

            elif opcao_menu_escolhida == "4":
                while True:
                    opcao_sair_escolhida = confirmacao_sair_do_jogo()

                    if opcao_sair_escolhida == "1":
                        saindo_do_jogo()
                        self.rodando = False
                        break

                    elif opcao_sair_escolhida == "2":
                        break

                    else:
                        opcao_invalida()

            else:
                opcao_invalida()


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