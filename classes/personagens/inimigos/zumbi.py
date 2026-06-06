# classes/personagens/inimigos/zumbi.py
from classes.personagens.inimigos.inimigo import Inimigo
from textos.movimentos import movimento_ataque

class Zumbi(Inimigo):
    def __init__(self, nome, vida, vida_max, dano, imagem, movimentos, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem, movimentos, fraqueza, imune)
        
    def realizar_ataque(self):
        movimento_ataque(self.nome, self.movimentos)
        return self.dano