# classes/jogo.py
import random
from classes.personagens.jogador import Jogador
from classes.loja import Loja
from instancias.fases import fases
from instancias.municoes import municao_bronze
from instancias.medicinas import antidoto
from audios.audio import parar_audio
from textos.menus import menu_combate, menu_principal, menu_status
from textos.inputs import input_recomecar_jogo, input_sair_do_jogo
from textos.introducoes import introducao_fase, introducao_jogo
from textos.mensagens import (
    mensagem_apareceu_inimigo, mensagem_concluiu_fase,
    mensagem_ganhou_moedas, mensagem_morreu,
    mensagem_nova_fase_desbloqueada, mensagem_opcao_invalida,
    mensagem_saindo_do_jogo, mensagem_venceu, mensagem_zerou_jogo
)
from rich.console import Console
from rich.panel import Panel
from textos.tela import passar_texto

console = Console()


class Jogo:
    def __init__(self):
        self.rodando = True
        self.jogador = None
        self.inimigo = None
        self.fases = fases
        self.fase_atual = 0
        self.fase_mostrar_cena = True

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

        for f in self.fases:
            for inimigo in f.inimigos:
                inimigo.vida = inimigo.vida_max

    def realizar_combate(self):
        inimigos_da_fase = self.buscar_fase()

        for inimigo_atual in inimigos_da_fase.inimigos:
            self.inimigo = inimigo_atual
            self.inimigo.vida = self.inimigo.vida_max

            mensagem_apareceu_inimigo(self.inimigo.nome)

            while self.jogador.esta_vivo() and self.inimigo.esta_vivo():
                while True:
                    console.clear()
                    status_txt = f"[bold green] Jogador:[/] {self.jogador.nome} | HP: [bold red]{self.jogador.vida}/{self.jogador.vida_max}[/] | Moedas: [bold yellow] {self.jogador.moedas}[/]\n" \
                                 f"[bold magenta] Inimigo:[/] {self.inimigo.nome} | HP: [bold red]{self.inimigo.vida}/{self.inimigo.vida_max}[/]"
                    console.print(Panel(status_txt, title=" STATUS DO COMBATE ", border_style="red"))

                    opcao_combate_escolhida = menu_combate(
                        self.jogador.nome,
                        self.inimigo.nome,
                        self.inimigo.vida,
                        self.inimigo.vida_max,
                        self.inimigo.imagem,
                        self.jogador.vida,
                        self.jogador.vida_max,
                        self.jogador.imagem
                    )

                    if opcao_combate_escolhida == "1":
                        ataque_realizado = self.jogador.atacar_com_municao(self.inimigo)
                        if not ataque_realizado:
                            continue
                        break

                    elif opcao_combate_escolhida == "2":
                        self.jogador.atacar_com_faca(self.inimigo)
                        break

                    elif opcao_combate_escolhida == "3":
                        medicina_utilizada = self.jogador.usar_medicina()
                        if not medicina_utilizada:
                            continue
                        break
                    else:
                        mensagem_opcao_invalida()

                if self.inimigo.esta_vivo():
                    self.jogador.regenerar()
                    dano_do_ataque = self.inimigo.realizar_ataque()
                    if dano_do_ataque > 0:
                        self.jogador.receber_dano(dano_do_ataque)

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
            return "zerou"

        jogar_fase = self.buscar_fase()
        resultado_combate = self.realizar_combate()

        if resultado_combate == "morreu":
            return "morreu"

        mensagem_concluiu_fase(jogar_fase.numero, jogar_fase.nome)
        self.fase_atual += 1

        if self.fase_atual >= len(self.fases):
            console.clear()
            mensagem_zerou_jogo()

            texto_vitoria = (
                "[bold green] PARABÉNS! VOCÊ SOBREVIVEU AO APOCALIPSE! [/]\n\n"
                "Você derrotou todas as ameaças, superou as adversidades\n"
                "e conseguiu escapar do sistema com vida.\n\n"
                "[bold green]Obrigado por jogar NecroSystem![/]"
            )
            console.print(Panel(
                texto_vitoria,
                title="[bold green] VITÓRIA [/]",
                border_style="green",
                expand=False
            ))
            input("\nPressione [Enter] para continuar...")
            return "zerou"

        else:
            mensagem_nova_fase_desbloqueada()
            self.fase_mostrar_cena = True
            passar_texto("")
            return "venceu"

    def iniciar_jogo(self):
        introducao_jogo()
        self.preparar_jogador()
        parar_audio()

        loja = Loja()

        while self.rodando:
            cena_fase = self.buscar_fase()
            if self.fase_mostrar_cena:
                descricao_verde = f"\033[1;32m{cena_fase.descricao}\033[0m"
                introducao_fase(cena_fase.imagem, descricao_verde)
                self.fase_mostrar_cena = False

            opcao_menu_escolhida = menu_principal(
                self.fase_atual,
                len(self.fases)
            )

            if opcao_menu_escolhida == "1":
                resultado = self.explorar_fases()

                if resultado == "morreu":
                    while True:
                        opcao_recomecar_escolhida = input_recomecar_jogo()
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

                elif resultado == "zerou":
                    while True:
                        # ✨ Pergunta se quer jogar de novo APÓS ver as mensagens de parabéns
                        opcao_recomecar_escolhida = input_recomecar_jogo()
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
                    opcao_sair_escolhida = input_sair_do_jogo()
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