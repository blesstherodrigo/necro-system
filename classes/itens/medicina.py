# classes/itens/medicina.py

class Medicina:
    def __init__(self, nome, efeito, bonus, preco, duracao="instantaneo"):
        self.nome = nome
        self.efeito = efeito
        self.bonus = bonus
        self.preco = preco
        self.duracao = duracao