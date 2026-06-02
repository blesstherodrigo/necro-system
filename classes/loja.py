# classes/loja.py
from instancias.municoes import municoes
from instancias.medicinas import medicinas
from textos.fixar_tela import limpar_tela, enter_continuar

class Loja:
    def __init__(self):
        self.catalogo_municao = municoes
        self.catalogo_medicina = medicinas

    def menu_comprar_itens(self, jogador):
        while True:
            limpar_tela()
            print("=== Comprar Itens ===")
            print(f"Moedas: {jogador.moedas}")
            print("-" * 25)
            print("=== Munições ===")
            for indice, municao in enumerate(self.catalogo_municao, start=1):
                print(
                    f"{indice}. {municao.tipo} | "
                    f"Dano: {municao.dano_base} | "
                    f"Crítico: {municao.dano_vantajoso} | "
                    f"Efetividade: {municao.efetividade} | "
                    f"Preço: {municao.preco}"
                )
            print("\n")
            print("=== Medicinas ===")
            for indice, medicina in enumerate(self.catalogo_medicina, start=6):
                print(
                    f"{indice}. {medicina.nome} | "
                    f"Efeito: {medicina.efeito} | "
                    f"Bônus: {medicina.bonus} | "
                    f"Preço: {medicina.preco}"
                )
            print("-" * 25)
            print("0. Voltar")
            escolha = int(input("Escolha um item: "))

            if escolha == 0:
                break

            elif escolha <= 5:
                try:
                    indice_escolha = escolha - 1
                    municao = self.catalogo_municao[indice_escolha]
                except (ValueError, IndexError):
                    print("Escolha inválida.")
                    enter_continuar()
                    continue

                try:
                    quantidade = int(input("Quantidade: "))
                except ValueError:
                    print("Quantidade inválida.")
                    enter_continuar()
                    continue

                # repetido???
                if quantidade <= 0:
                    print("Quantidade inválida.")
                    enter_continuar()
                    continue

                preco_total_municoes = municao.preco * quantidade
                if preco_total_municoes > jogador.moedas:
                    print("Você não tem moedas suficientes.")
                else:
                    jogador.moedas -= preco_total_municoes
                    jogador.mochila.adicionar_item(municao, quantidade)
                    print(f"Você comprou {quantidade}x {municao.tipo}.")
                enter_continuar()

            elif escolha >= 5:
                try:
                    indice_escolha = int(escolha) - 6
                    medicina = self.catalogo_medicina[indice_escolha]
                except (ValueError, IndexError):
                    print("Escolha inválida.")
                    enter_continuar()
                    continue

                try:
                    quantidade = int(input("Quantidade: "))
                except ValueError:
                    print("Quantidade inválida.")
                    enter_continuar()
                    continue

                # repetido???
                if quantidade <= 0:
                    print("Quantidade inválida.")
                    enter_continuar()
                    continue

                preco_total = medicina.preco * quantidade
                if preco_total > jogador.moedas:
                    print("Você não tem moedas suficientes.")
                else:
                    jogador.moedas -= preco_total
                    jogador.mochila.adicionar_item(medicina, quantidade)
                    print(f"Você comprou {quantidade}x {medicina.nome}.")
                enter_continuar()

    def menu_vender_itens(self, jogador):
        while True:
            limpar_tela()
            print("=== Vender Itens ===")
            print(f"Moedas: {jogador.moedas}")
            print("-" * 25)

            itens_disponiveis = [
                item for item, quantidade in jogador.mochila.itens.items()
                if quantidade > 0
            ]

            if not itens_disponiveis:
                print("Você não tem itens para vender.")
                enter_continuar()
                break

            for indice, item in enumerate(itens_disponiveis, start=1):
                quantidade = jogador.mochila.itens[item]
                nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
                preco = getattr(item, "preco", 0)
                preco_venda = preco // 2

                print(
                    f"{indice}. {nome} "
                    f"({quantidade}) | "
                    f"Venda: {preco_venda} moedas"
                )

            print("0. Voltar")
            print("-" * 25)

            escolha = input("Escolha um item para vender: ")

            if escolha == "0":
                break

            try:
                indice_escolha = int(escolha) - 1
                item = itens_disponiveis[indice_escolha]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                enter_continuar()
                continue

            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida.")
                enter_continuar()
                continue

            if quantidade <= 0:
                print("Quantidade inválida.")
                enter_continuar()
                continue

            quantidade_atual = jogador.mochila.itens[item]

            if quantidade > quantidade_atual:
                print("Você não tem essa quantidade.")
                enter_continuar()
                continue

            preco = getattr(item, "preco", 0)
            preco_venda = preco // 2
            total_venda = preco_venda * quantidade

            jogador.mochila.remover_item(item, quantidade)
            jogador.moedas += total_venda

            nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
            print(f"Você vendeu {quantidade}x {nome} por {total_venda} moedas.")
            enter_continuar()

    def abrir_loja(self, jogador):
        while True:
            limpar_tela()
            print("=== LOJA ===")
            print(f"Moedas: {jogador.moedas}")
            print("-" * 25)
            print("1. Comprar")
            print("2. Vender")
            print("0. Voltar")
            print("-" * 25)

            escolha = input("> ")

            if escolha == "1":
                self.menu_comprar_itens(jogador)
            elif escolha == "2":
                self.menu_vender_itens(jogador)
            elif escolha == "0":
                break
            else:
                print("Opção inválida.")
                enter_continuar()