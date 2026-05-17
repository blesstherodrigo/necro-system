# classes/personagens/jogador.py
from classes.personagens.personagem import Personagem
from game.textos.fixar_tela import limpar_tela

class Jogador(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem):
        super().__init__(nome, vida, vida_max, dano, imagem)

    def atacar(self, inimigo):
        super().atacar(inimigo)
        limpar_tela()
        print(f"{self.nome} usou a faca e causou {self.dano} de dano")