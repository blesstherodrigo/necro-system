# classes/jogo.py
from classes.personagens.jogador import Jogador
from data.fases import fase_1, fase_2, fase_3, fase_4

from game.textos.menus import menu_combate, menu_principal, menu_status, menu_mochila
from game.textos.confirmacoes import confirmacao_sair_do_jogo, confirmacao_recomecar_jogo
from game.textos.inputs import receber_escolha_personagem, receber_nome_do_jogdor
from game.textos.introducoes import introducao_fase
from game.textos.mensagens import (
    mensagem_opcao_invalida, mensagem_apareceu_inimigo,
    mensagem_concluiu_fase, mensagem_nova_fase_desbloqueada,
    mensagem_venceu, mensagem_morreu, mensagem_recuou,
    mensagem_zerou_jogo, mensagem_saindo_do_jogo
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
            personagem_escolhido = receber_escolha_personagem()

            if personagem_escolhido == "1":
                imagem = "imgem do jogador homem aqui"
                break
            elif personagem_escolhido == "2":
                imagem = "imagem do jogador mulher aqui"
                break
            else:
                mensagem_opcao_invalida()

        nome = receber_nome_do_jogdor()
        self.jogador = Jogador(nome, 1000, 1000, 50, imagem)

    def buscar_fases(self):
        buscar_fase_atual = self.fases[self.fase_atual]
        return buscar_fase_atual

    # criar combates para tipos diferentes de inimigos (zumbi comum e boss)
    def combate(self):
        inimigos_fase = self.buscar_fases()

        for buscar_inimigo in inimigos_fase["inimigos"]:
            self.inimigo = buscar_inimigo

            mensagem_apareceu_inimigo(self.inimigo.nome)

            while self.jogador.esta_vivo() and self.inimigo.esta_vivo():
                opcao_combate_escolhida = menu_combate(
                    self.inimigo.nome,
                    self.inimigo.vida,
                    self.inimigo.vida_max,
                    self.jogador.vida,
                    self.jogador.vida_max
                )

                if opcao_combate_escolhida == "1":
                    self.jogador.atacar(self.inimigo)

                    if self.inimigo.esta_vivo():
                        self.inimigo.atacar(self.jogador)

                elif opcao_combate_escolhida == "2":
                    mensagem_recuou()
                    return "fugiu"

                else:
                    mensagem_opcao_invalida()

            if not self.jogador.esta_vivo():
                mensagem_morreu()
                return "morreu"

            mensagem_venceu(self.inimigo.nome)
        return "venceu"

    def explorar_fases(self):
        if self.fase_atual >= len(self.fases):
            mensagem_zerou_jogo()
            return "finalizado"

        jogar_fase = self.buscar_fases()

        introducao_fase(jogar_fase['numero'], jogar_fase['nome'], jogar_fase["descricao"])

        resultado_combate = self.combate()      # iniciar combate

        if resultado_combate == "morreu":
            return "morreu"

        if resultado_combate == "fugiu":
            return "fugiu"

        mensagem_concluiu_fase(jogar_fase["numero"], jogar_fase["nome"])
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            mensagem_zerou_jogo()
        else:
            mensagem_nova_fase_desbloqueada()
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
            opcao_menu_escolhida = menu_principal(
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
                            mensagem_saindo_do_jogo()
                            self.rodando = False
                            break
                        else:
                            mensagem_opcao_invalida()

            elif opcao_menu_escolhida == "2":
                menu_status(
                    self.jogador.nome,
                    self.jogador.vida,
                    self.jogador.vida_max,
                    self.jogador.dano
                )

            elif opcao_menu_escolhida == "3":
                menu_mochila()

            elif opcao_menu_escolhida == "4":
                while True:
                    opcao_sair_escolhida = confirmacao_sair_do_jogo()

                    if opcao_sair_escolhida == "1":
                        mensagem_saindo_do_jogo()
                        self.rodando = False
                        break
                    elif opcao_sair_escolhida == "2":
                        break
                    else:
                        mensagem_opcao_invalida()

            else:
                mensagem_opcao_invalida()