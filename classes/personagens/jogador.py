# classes/personagens/jogador.py
from classes.personagens.personagem import Personagem
from classes.itens.mochila import Mochila
from classes.itens.municao import Municao
from classes.itens.medicina import Medicina

from textos.tela import enter_continuar, enter_voltar, limpar_tela, limpar_intervalo, passar_texto
from textos.inputs import input_escolha_personagem, input_nome_do_jogdor
from textos.mensagens import mensagem_opcao_invalida, mensagem_recebeu_dano, mensagem_digite_nome
from textos.artes.arte import mostrar_artes_lado_a_lado
from textos.movimentos import movimento_ataque, movimento_usar_adrenalina, movimento_usar_antidoto, movimento_usar_soro, movimento_usar_analgesico
from textos.menus import menu_escolher_municao, menu_escolher_medicina

class Jogador(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem, mochila, moedas):
        super().__init__(nome, vida, vida_max, dano, imagem)
        self.mochila = mochila
        self.moedas = moedas
        self.dano_bonus = 0
        self.defesa_bonus = 0
        self.regeneracao = 0

    @staticmethod
    def criar_jogador():
        while True:
            while True:
                nome = input_nome_do_jogdor()
                if len(nome) < 1:
                    mensagem_digite_nome()
                else:
                    break

            limpar_tela()
            mostrar_artes_lado_a_lado("jogador_homem.txt", "jogador_mulher.txt")
            escolha = input_escolha_personagem()

            if escolha == "1":
                imagem = "jogador_homem.txt"
                break
            elif escolha == "2":
                imagem = "jogador_mulher.txt"
                break
            else:
                mensagem_opcao_invalida()

        return Jogador(nome, 100, 100, 10, imagem, Mochila(), 50)

    def atacar_com_municao(self, inimigo):
        municao = self.escolher_municao()

        if municao is None:
            return False

        inimigo.receber_dano_municao(municao)
        return True

    def atacar_com_faca(self, inimigo):
        dano = self.dano + self.dano_bonus
        movimento_ataque(self.nome, "Facada")
        inimigo.receber_dano_faca(dano)

    def escolher_municao(self):
        municao_disponivel = [
            item
            for item, quantidade in self.mochila.itens.items()
            if isinstance(item, Municao) and quantidade > 0
        ]

        if not municao_disponivel:
            passar_texto("Você não tem munição!")
            enter_voltar()
            return None

        while True:
            try:
                escolha = menu_escolher_municao(municao_disponivel, self.mochila.itens)

                if escolha == 0:
                    return None

                limpar_intervalo(40, 40 + len(municao_disponivel) + 3)

                municao = municao_disponivel[escolha - 1]
            except (ValueError, IndexError):
                mensagem_opcao_invalida()
                return None

            if self.mochila.remover_item(municao, 1):
                return municao

            return None

    def escolher_medicina(self):
        medicinas_disponiveis = [
            item
            for item, quantidade in self.mochila.itens.items()
            if isinstance(item, Medicina) and quantidade > 0
        ]

        if not medicinas_disponiveis:
            passar_texto("Você não tem medicinas!")
            enter_voltar()
            return None

        while True:
            try:
                escolha = menu_escolher_medicina(medicinas_disponiveis, self.mochila.itens)

                if escolha == 0:
                    return None

                limpar_intervalo(40, 40 + len(medicinas_disponiveis) + 3)

                medicina = medicinas_disponiveis[escolha - 1]
            except (ValueError, IndexError):
                mensagem_opcao_invalida()
                enter_voltar()
                return None

            if self.mochila.remover_item(medicina, 1):
                return medicina

            return None

    def curar(self, quantidade):
        self.vida += quantidade
        if self.vida > self.vida_max:
            self.vida = self.vida_max

    # este metodo é útil para o efeito do Soro (utilizado no combate da classe Jogo)
    def regenerar(self):
        if self.regeneracao > 0:
            self.curar(self.regeneracao)

    def usar_medicina(self):
        medicina = self.escolher_medicina()

        if medicina is None:
            return False

        if medicina.nome == "Adrenalina":
            self.dano_bonus += medicina.bonus
            movimento_usar_adrenalina(self.nome, medicina.nome, medicina.bonus)

        elif medicina.nome == "Antídoto":
            self.curar(medicina.bonus)
            movimento_usar_antidoto(self.nome, medicina.nome, medicina.bonus)

        elif medicina.nome == "Soro":
            self.regeneracao += medicina.bonus
            movimento_usar_soro(self.nome, medicina.nome, medicina.bonus)

        elif medicina.nome == "Analgésico":
            self.defesa_bonus += medicina.bonus
            movimento_usar_analgesico(self.nome, medicina.nome, medicina.bonus)
        enter_continuar()
        return True

    def receber_dano(self, dano):
        dano_final = dano - self.defesa_bonus

        if dano_final < 0:
            dano_final = 0

        super().receber_dano(dano_final)
        mensagem_recebeu_dano(self.nome, dano_final)

    def resetar_efeitos_luta(self):
        self.dano_bonus = 0
        self.defesa_bonus = 0
        self.regeneracao = 0