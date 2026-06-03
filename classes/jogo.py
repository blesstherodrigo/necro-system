# classes/jogo.py
import random
from classes.personagens.jogador import Jogador
from classes.loja import Loja
from instancias.fases import fases
from instancias.municoes import municao_bronze
from instancias.medicinas import antidoto
from audios.audio import parar_audio
from textos.menus import menu_combate, menu_principal, menu_status
from textos.confirmacoes import confirmacao_sair_do_jogo, confirmacao_recomecar_jogo
from textos.introducoes import introducao_jogo, introducao_fase
from textos.cutscenes import exemplo_cutscene
from textos.mensagens import (
    mensagem_opcao_invalida, mensagem_apareceu_inimigo,
    mensagem_concluiu_fase, mensagem_nova_fase_desbloqueada,
    mensagem_venceu, mensagem_morreu, mensagem_ganhou_moedas,
    mensagem_zerou_jogo, mensagem_saindo_do_jogo
)

class Jogo:
    def __init__(self):
        self.rodando = True
        self.jogador = None
        self.inimigo = None
        self.fases = fases
        self.fase_atual = 0

    def preparar_jogador(self):
        self.jogador = Jogador.criar_jogador()
        self.jogador.mochila.adicionar_item(municao_bronze, 5)
        self.jogador.mochila.adicionar_item(antidoto, 1)

    def buscar_fase(self):
        buscar_fase_atual = self.fases[self.fase_atual]
        return buscar_fase_atual

    def reiniciar_jogo(self):
        self.rodando = True
        self.jogador = None
        self.inimigo = None
        self.fase_atual = 0

    # combates para tipos diferentes de inimigos (zumbi comum e boss)???
    def realizar_combate(self):
        inimigos_da_fase = self.buscar_fase()

        for inimigo_atual in inimigos_da_fase.inimigos:
            self.inimigo = inimigo_atual
            mensagem_apareceu_inimigo(self.inimigo.nome)

            while self.jogador.esta_vivo() and self.inimigo.esta_vivo():
                while True:
                    opcao_combate_escolhida = menu_combate(
                        self.inimigo.nome,
                        self.inimigo.vida,
                        self.inimigo.vida_max,
                        self.inimigo.imagem,
                        self.jogador.vida,
                        self.jogador.vida_max,
                        self.jogador.imagem
                    )

                    if opcao_combate_escolhida == "1":
                        municao = self.jogador.escolher_municao()

                        if municao is None:
                            continue

                        self.inimigo.receber_dano_municao(municao)
                        break

                    elif opcao_combate_escolhida == "2":
                        self.jogador.atacar_com_faca(self.inimigo)
                        break

                    elif opcao_combate_escolhida == "3":
                        medicina = self.jogador.escolher_medicina()

                        if medicina is None:
                            continue

                        self.jogador.usar_medicina(medicina)
                        break

                    else:
                        mensagem_opcao_invalida()

                if self.inimigo.esta_vivo():
                    self.jogador.regenerar()
                    dano_do_ataque = self.inimigo.realizar_ataque() # Mudanças para utilizar ataques únicos de cada zumbi existente
                    self.jogador.receber_dano(dano_do_ataque)

            # recompensas por fase ou por combate???
            if self.jogador.esta_vivo():
                self.jogador.resetar_efeitos_luta()
                recompensa = random.randint(15, 35)
                self.jogador.moedas += recompensa
                mensagem_venceu(self.inimigo.nome)
                mensagem_ganhou_moedas(recompensa)
            else:
                mensagem_morreu()
                return "morreu"

        return "venceu"

    def explorar_fases(self):
        if self.fase_atual >= len(self.fases):
            mensagem_zerou_jogo()
            while True:
                opcao_recomecar_escolhida = confirmacao_recomecar_jogo()

                if opcao_recomecar_escolhida == "1":
                    introducao_jogo()
                    self.reiniciar_jogo()
                    self.preparar_jogador()
                    parar_audio()
                    break
                elif opcao_recomecar_escolhida == "2":
                    return "zerou"
                else:
                    mensagem_opcao_invalida()

        jogar_fase = self.buscar_fase()

        introducao_fase(jogar_fase.numero, jogar_fase.nome, jogar_fase.imagem, jogar_fase.descricao)

        resultado_combate = self.realizar_combate()      # inicia o combate

        if resultado_combate == "morreu":
            return "morreu"

        if resultado_combate == "fugiu":
            return "fugiu"

        mensagem_concluiu_fase(jogar_fase.numero, jogar_fase.nome)
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            mensagem_zerou_jogo()
        else:
            mensagem_nova_fase_desbloqueada()
            exemplo_cutscene()
            return "venceu"

    def iniciar_jogo(self):
        introducao_jogo()
        self.preparar_jogador()
        parar_audio()
        loja = Loja()

        while self.rodando:
            opcao_menu_escolhida = menu_principal(
                self.fase_atual,
                len(self.fases)
            )

            if opcao_menu_escolhida == "1":
                resultado = self.explorar_fases()

                if resultado == "morreu":
                    while True:
                        opcao_recomecar_escolhida = confirmacao_recomecar_jogo()

                        if opcao_recomecar_escolhida == "1":
                            introducao_jogo()
                            self.reiniciar_jogo()
                            self.preparar_jogador()
                            parar_audio()
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
                loja.abrir_loja(self.jogador)

            elif opcao_menu_escolhida == "4":
                self.jogador.mochila.mostrar_mochila()

            elif opcao_menu_escolhida == "5":
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