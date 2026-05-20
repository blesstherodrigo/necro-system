# classes/personagens/jogador.py
from classes.personagens.personagem import Personagem
from classes.itens.mochila import Mochila
from textos.inputs import input_escolha_personagem, input_nome_do_jogdor
from textos.mensagens import mensagem_opcao_invalida
from textos.fixar_tela import enter_continuar, enter_voltar

class Jogador(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem, mochila, moedas):
        super().__init__(nome, vida, vida_max, dano, imagem)
        self.mochila = mochila
        self.moedas = moedas

    @staticmethod
    def criar_jogador():
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

        nome = input_nome_do_jogdor()

        return Jogador(nome, 100, 100, 10, imagem, Mochila(), 50)

    def escolher_municao(self):
        municao_disponivel = [
            municao
            for municao, quantidade in self.mochila.itens.items()
            if quantidade > 0
        ]

        if not municao_disponivel:
            print("Você não tem munição!")
            enter_voltar()
            return None

        print("\nEscolha a munição:")
        for indice, municao in enumerate(municao_disponivel, start=1):
            quantidade = self.mochila.itens[municao]
            print(f"{indice}. {municao.tipo} ({quantidade})")

        try:
            escolha = int(input("> ")) - 1
            municao = municao_disponivel[escolha]
        except (ValueError, IndexError):
            print("Escolha inválida.")
            return None

        if self.mochila.usar_municao(municao):
            return municao

        return None

    def receber_dano(self, dano):
        super().receber_dano(dano)
        print(f"\nVocê recebeu {dano} de dano. Sua vida: {self.vida}")
        enter_continuar()