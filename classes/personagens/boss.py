# classes/personagens/boss.py

from classes.personagens.personagem import Personagem

# subclasse de Personagem
class Boss(Personagem):
    def __init__(self, nome, vida, vida_max, dano):
        super().__init__(nome, vida, vida_max, dano)

    def atacar(self, alvo):
        super().atacar(alvo)
        print(f"{self.nome} desferiu um ataque pesado e causou {self.dano} de dano")
