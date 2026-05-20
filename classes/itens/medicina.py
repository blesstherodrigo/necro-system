# classes/itens/medicina.py

class Medicina:
    def __init__(self, nome, tipo, valor, preco, duracao="instantaneo"):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor
        self.preco = preco
        self.duracao = duracao