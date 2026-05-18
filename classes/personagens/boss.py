# classes/personagens/boss.py
from classes.personagens.inimigo import Inimigo

class Boss(Inimigo):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem, fraqueza, imune)