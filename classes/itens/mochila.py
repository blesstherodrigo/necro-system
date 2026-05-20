# classes/itens/mochila.py
from textos.fixar_tela import enter_voltar

class Mochila:
    def __init__(self):
        self.itens = {}

    def adicionar_municao(self, municao, quantidade):
        if municao not in self.itens:
            self.itens[municao] = 0
        self.itens[municao] += quantidade

    def usar_municao(self, municao):
        if self.itens.get(municao, 0) > 0:
            self.itens[municao] -= 1
            return True
        return False

    def mostrar_mochila(self):
        print("\n=== Mochila ===")
        if not self.itens:
            print("Você não tem munições.")
            return

        for municao, quantidade in self.itens.items():
            print(f"{municao.tipo}: {quantidade}")

        enter_voltar()