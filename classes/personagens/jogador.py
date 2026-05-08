from classes.personagens.personagem import Personagem

# subclasse de Personagem
class Jogador(Personagem):
    def __init__(self, nome, vida, vida_max, dano):
        super().__init__(nome, vida, vida_max, dano)

    def atacar(self, alvo):
        super().atacar(alvo)
        print(f"Você deu uma facada em {alvo.nome} e causou {self.dano} de dano")        