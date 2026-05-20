# classes/itens/mochila.py
from textos.fixar_tela import enter_voltar

class Mochila:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item, quantidade):
        if item not in self.itens:
            self.itens[item] = 0
        self.itens[item] += quantidade

    def remover_item(self, item, quantidade):
        if self.itens.get(item, 0) >= quantidade:
            self.itens[item] -= quantidade

            if self.itens[item] <= 0:
                del self.itens[item]

            return True

        return False

    def mostrar_mochila(self):
        print("\n=== Mochila ===")

        if not self.itens:
            print("Você não tem itens.")
            return

        for item, quantidade in self.itens.items():
            nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
            print(f"{nome}: {quantidade}")

        enter_voltar()