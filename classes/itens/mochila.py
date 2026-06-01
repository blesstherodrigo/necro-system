# classes/itens/mochila.py
from textos.menus import menu_mochila

class Mochila:
    def __init__(self):
        self.itens = {}

    def mostrar_mochila(self):
        menu_mochila(self.itens)

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