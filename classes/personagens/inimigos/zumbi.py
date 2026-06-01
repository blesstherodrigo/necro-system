# classes/personagens/inimigos/zumbi.py
from classes.personagens.inimigos.inimigo import Inimigo

class Zumbi(Inimigo):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem, fraqueza, imune)
        
    def realizar_ataque(self):
        print(f"{self.nome} arranhou e causou {self.dano} de dano!")
        return self.dano