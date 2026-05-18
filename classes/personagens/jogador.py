# classes/personagens/jogador.py
from classes.personagens.personagem import Personagem

from game.textos.fixar_tela import limpar_tela

class Jogador(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem, mochila, moedas):
        super().__init__(nome, vida, vida_max, dano, imagem)
        self.mochila = mochila
        self.moedas = moedas

    def receber_dano(self, dano):
        super().receber_dano(dano)
        limpar_tela()
        print(f"Você recebeu {dano} de dano. Sua vida: {self.vida}")