# classes/itens/mochila.py
from game.textos.fixar_tela import enter_voltar

class Mochila:
    def __init__(self):
        self.itens = {}

    def add_municao(self, municao_nome, quantidade):
        if municao_nome not in self.itens:
            self.itens[municao_nome] = 0
        self.itens[municao_nome] += quantidade

    def usar_municao(self, municao_nome):
        if self.itens.get(municao_nome, 0) > 0:
            self.itens[municao_nome] -= 1
            return True
        return False

    def mostrar(self):
        print("\n=== Mochila ===")
        if not self.itens:
            print("Você não tem munições.")
            return

        for municao_nome, quantidade in self.itens.items():
            print(f"{municao_nome}: {quantidade}")

        enter_voltar()