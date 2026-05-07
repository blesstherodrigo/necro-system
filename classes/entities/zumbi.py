from classes.entities.personagem import Personagem

class Zumbi(Personagem):
    def __init__(self, nome, vida, vida_max, dano):
        super().__init__(nome, vida, vida_max, dano)