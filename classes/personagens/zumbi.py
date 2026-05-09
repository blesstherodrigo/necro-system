# classes/personagens/zumbi.py

from classes.personagens.personagem import Personagem

# subclasse de Personagem
class Zumbi(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem):
        super().__init__(nome, vida, vida_max, dano, imagem)

    def atacar(self, alvo):
        super().atacar(alvo)
        print(f"{self.nome} te arranhou e causou {self.dano} de dano")