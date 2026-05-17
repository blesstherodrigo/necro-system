# classes/personagens/zumbi.py
from classes.personagens.personagem import Personagem
from game.textos.fixar_tela import enter_continuar

class Zumbi(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem):
        super().__init__(nome, vida, vida_max, dano, imagem)

    def atacar(self, inimigo):
        super().atacar(inimigo)
        print(f"{self.nome} te arranhou e causou {self.dano} de dano")
        enter_continuar()