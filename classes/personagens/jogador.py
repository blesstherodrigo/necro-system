# classes/personagens/jogador.py
from classes.personagens.personagem import Personagem
from classes.itens.mochila import Mochila
from classes.itens.municao import Municao
from classes.itens.medicina import Medicina

from textos.fixar_tela import enter_continuar, enter_voltar
from textos.inputs import input_escolha_personagem, input_nome_do_jogdor
from textos.mensagens import mensagem_opcao_invalida, mensagem_recebeu_dano

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
        nome = input_nome_do_jogdor()

        # aqui deve mostrar a imagem dos personagens, Homem e Mulher
        while True:
            escolha = input_escolha_personagem()

            if escolha == "1":
                imagem = "imagem do jogador homem aqui"
                break
            elif escolha == "2":
                imagem = "imagem do jogador mulher aqui"
                break
            else:
                mensagem_opcao_invalida()

        return Jogador(nome, 100, 100, 10, imagem, Mochila(), 50)

    def escolher_municao(self):
        municao_disponivel = [
            item
            for item, quantidade in self.mochila.itens.items()
            if isinstance(item, Municao) and quantidade > 0
        ]

        if not municao_disponivel:
            print("Você não tem munição!")
            enter_voltar()
            return None

        while True:
            print("\nEscolha a munição:")

            print("0. Voltar")
            for indice, municao in enumerate(municao_disponivel, start=1):
                quantidade = self.mochila.itens[municao]
                print(f"{indice}. {municao.tipo} ({quantidade})")

            try:
                escolha = int(input("> "))
                if escolha == 0:
                    break
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
            print("Você não tem medicinas!")
            enter_voltar()
            return None

        while True:
            print("\nEscolha a medicina:")

            print("0. Voltar")
            for indice, medicina in enumerate(medicinas_disponiveis, start=1):
                quantidade = self.mochila.itens[medicina]
                print(
                    f"{indice}. {medicina.nome} "
                    f"({quantidade}) | Efeito: {medicina.tipo} | Valor: {medicina.valor}"
                )

            try:
                escolha = int(input("> "))
                if escolha == 0:
                    break
                medicina = medicinas_disponiveis[escolha - 1]
            except (ValueError, IndexError):
                mensagem_opcao_invalida()
                enter_voltar()
                return None

            if self.mochila.remover_item(medicina, 1):
                return medicina

            return None

    def receber_dano(self, dano):
        dano_final = dano - self.defesa_bonus

        if dano_final < 0:
            dano_final = 0

        super().receber_dano(dano_final)
        mensagem_recebeu_dano(self.nome, dano_final)
        enter_continuar()

    def dano_total(self):
        return self.dano + self.dano_bonus

    def atacar_com_faca(self, inimigo):
        dano = self.dano_total()
        inimigo.receber_dano_bruto(dano)

    # cura nao completa vida total se a vida estiver perto do limite
    def curar(self, quantidade):
        self.vida += quantidade
        if self.vida > self.vida_max:
            self.vida = self.vida_max

    def regenerar(self):
        if self.regeneracao > 0:
            self.curar(self.regeneracao)
            print(f"\n{self.nome} regenerou {self.regeneracao} de vida.")

    def resetar_efeitos_luta(self):
        self.dano_bonus = 0
        self.defesa_bonus = 0
        self.regeneracao = 0

    def usar_medicina(self, medicina):
        if medicina.tipo == "buff_dano":
            self.dano_bonus += medicina.valor
            print(f"\n{self.nome} usou {medicina.nome}. Dano aumentado em {medicina.valor} pelo resto da luta.")

        elif medicina.tipo == "cura_instantanea":
            self.curar(medicina.valor)
            print(f"\n{self.nome} usou {medicina.nome}. Recuperou {medicina.valor} de vida.")

        elif medicina.tipo == "regeneracao":
            self.regeneracao += medicina.valor
            print(f"\n{self.nome} {medicina.nome}. Vai regenerar {medicina.valor} de vida por turno.")

        elif medicina.tipo == "buff_defesa":
            self.defesa_bonus += medicina.valor
            print(f"\n{self.nome} {medicina.nome}. Defesa aumentada em {medicina.valor} pelo resto da luta.")

        enter_continuar()