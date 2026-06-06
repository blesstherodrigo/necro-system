# classes/loja.py
from instancias.municoes import municoes
from instancias.medicinas import medicinas
from textos.tela import enter_continuar
from textos.menus import menu_loja_comprar, menu_loja_vender, menu_loja
from textos.inputs import input_quantidade
from textos.mensagens import (
    mensagem_opcao_invalida,
    mensagem_sem_moedas_suficiente,
    mensagem_comprou_item,
    mensagem_vendeu_item,
    mensagem_sem_itens,
    mensagem_sem_quantidade
)

class Loja:
    def __init__(self):
        self.catalogo_municao = municoes
        self.catalogo_medicina = medicinas

    def comprar_municao(self, escolha, jogador):
        indice_escolha = escolha - 1

        try:
            municao = self.catalogo_municao[indice_escolha]
        except IndexError:
            mensagem_opcao_invalida()
            return True

        try:
            quantidade = input_quantidade()
        except ValueError:
            mensagem_opcao_invalida()
            return True

        if quantidade <= 0:
            mensagem_opcao_invalida()
            return True

        preco_total = municao.preco * quantidade

        if preco_total > jogador.moedas:
            mensagem_sem_moedas_suficiente()
        else:
            jogador.moedas -= preco_total
            jogador.mochila.adicionar_item(municao, quantidade)
            mensagem_comprou_item(quantidade, municao.tipo)
            return True

    def comprar_medicina(self, escolha, jogador):
        indice_escolha = escolha - len(self.catalogo_municao) - 1

        try:
            medicina = self.catalogo_medicina[indice_escolha]
        except IndexError:
            mensagem_opcao_invalida()
            return True

        try:
            quantidade = input_quantidade()
        except ValueError:
            mensagem_opcao_invalida()
            return True

        if quantidade <= 0:
            mensagem_opcao_invalida()
            return True

        preco_total = medicina.preco * quantidade

        if preco_total > jogador.moedas:
            mensagem_sem_moedas_suficiente()
            enter_continuar()
            return True

        jogador.moedas -= preco_total
        jogador.mochila.adicionar_item(medicina, quantidade)
        mensagem_comprou_item(quantidade, medicina.nome)
        return True

    def comprar_item(self, jogador):
        while True:
            escolha = menu_loja_comprar(
                jogador.moedas,
                self.catalogo_municao,
                self.catalogo_medicina
            )

            if escolha is None:
                mensagem_opcao_invalida()
                continue

            if escolha == 0:
                break

            total_municoes = len(self.catalogo_municao)
            total_itens = len(self.catalogo_municao) + len(self.catalogo_medicina)

            if 1 <= escolha <= total_municoes:
                self.comprar_municao(escolha, jogador)

            elif total_municoes < escolha <= total_itens:
                self.comprar_medicina(escolha, jogador)

            else:
                mensagem_opcao_invalida()

    @staticmethod
    def vender_item(jogador):
        while True:
            itens_disponiveis = [
                item for item, quantidade in jogador.mochila.itens.items()
                if quantidade > 0
            ]

            if not itens_disponiveis:
                mensagem_sem_itens()
                break

            escolha = menu_loja_vender(
                jogador.moedas,
                itens_disponiveis,
                jogador.mochila.itens
            )

            if escolha is None:
                mensagem_opcao_invalida()
                continue

            if escolha == 0:
                break

            if escolha < 1 or escolha > len(itens_disponiveis):
                mensagem_opcao_invalida()
                continue

            indice_escolha = escolha - 1
            item = itens_disponiveis[indice_escolha]

            try:
                quantidade = input_quantidade()
            except ValueError:
                mensagem_opcao_invalida()
                continue

            if quantidade <= 0:
                mensagem_opcao_invalida()
                continue

            quantidade_atual = jogador.mochila.itens[item]

            if quantidade > quantidade_atual:
                mensagem_sem_quantidade()
                continue

            preco = getattr(item, "preco", 0)
            preco_venda = preco // 2
            total_venda = preco_venda * quantidade

            jogador.mochila.remover_item(item, quantidade)
            jogador.moedas += total_venda

            nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
            mensagem_vendeu_item(quantidade, nome, total_venda)

    def abrir_loja(self, jogador):
        while True:
            try:
                escolha = menu_loja(jogador.moedas)
            except ValueError:
                mensagem_opcao_invalida()
                continue

            if escolha == 1:
                self.comprar_item(jogador)
            elif escolha == 2:
                self.vender_item(jogador)
            elif escolha == 0:
                break
            else:
                mensagem_opcao_invalida()