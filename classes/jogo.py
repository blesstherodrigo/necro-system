# classes/jogo.py
from classes.personagens.jogador import Jogador
from data.fases import fase_1, fase_2, fase_3, fase_4
from game.textos import (
    limpar_tela,
    enter_continuar,
    opcao_invalida,
    saindo_do_jogo,
    mostrar_menu,
    mostrar_status,
    mostrar_mochila,
    confirmacao_sair_do_jogo,
    confirmacao_recomecar_jogo,
    introducao_fase,
    mostrar_combate,
    recuou_do_combate,
    escolher_personagem,
    digitar_nome_do_jogdor
)

class Jogo:
    def __init__(self):
        self.rodando = True
        self.jogador = None
        self.inimigo = None
        self.fases = [fase_1, fase_2, fase_3, fase_4]
        self.fase_atual = 0

    def criar_jogador(self):
        # aqui deve mostrar a imagem dos personagens, Homem e Mulher

        while True:
            escolha = escolher_personagem()

            if escolha == "1":
                imagem = "imgem do jogador homem aqui"
                break
            elif escolha == "2":
                imagem = "imagem do jogador mulher aqui"
                break
            else:
                opcao_invalida()

        nome = digitar_nome_do_jogdor()
        self.jogador = Jogador(nome, 1, 1000, 1, imagem)

    def buscar_fases(self):
        buscar_fase_atual = self.fases[self.fase_atual]
        return buscar_fase_atual

    # criar combates para tipos diferentes de inimigos (zumbi comum e boss)
    def combate(self):
        inimigos_fase = self.buscar_fases()

        for buscar_inimigo in inimigos_fase["inimigos"]:
            self.inimigo = buscar_inimigo

            limpar_tela()
            print(f"Um {self.inimigo.nome} apareceu!")
            enter_continuar()

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

            if not self.jogador.esta_vivo():
                print("\nVocê morreu.")
                enter_continuar()
                return "morreu"

            print(f"\nVocê derrotou {self.inimigo.nome}!")
            enter_continuar()

        return "venceu"

    def explorar_fases(self):
        if self.fase_atual >= len(self.fases):
            limpar_tela()
            print("\nVocê já concluiu todas as fases disponíveis!")
            enter_continuar()
            return "finalizado"

        jogar_fase = self.buscar_fases()
        introducao_fase(jogar_fase['numero'], jogar_fase['nome'], jogar_fase["descricao"])
        resultado_combate = self.combate()      # combate aqui

        if resultado_combate == "morreu":
            return "morreu"

        if resultado_combate == "fugiu":
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

    def reiniciar_jogo(self):
        self.rodando = True
        self.jogador = None
        self.inimigo = None
        self.fase_atual = 0
        self.criar_jogador()

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
                    while True:
                        opcao_recomecar_escolhida = confirmacao_recomecar_jogo()

                        if opcao_recomecar_escolhida == "1":
                            self.reiniciar_jogo()
                            break
                        elif opcao_recomecar_escolhida == "2":
                            saindo_do_jogo()
                            self.rodando = False
                            break
                        else:
                            opcao_invalida()

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