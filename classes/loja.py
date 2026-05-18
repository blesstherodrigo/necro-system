from game.textos.fixar_tela import limpar_tela

class Loja:
    def __init__(self, catalogo_municao):
        self.catalogo_municao = catalogo_municao

    def mostrar_itens(self):
        limpar_tela()
        print("\n=== Loja do Mercante ===")
        for indice, municao in enumerate(self.catalogo_municao.values(), start=1):
            print(
                f"{indice}. {municao.tipo} | "
                f"Dano: {municao.dano_base} | "
                f"Crítico: {municao.dano_vantajoso} | "
                f"Preço: {municao.preco}"
            )

    def comprar_itens(self, jogador):
        while True:
            self.mostrar_itens()
            print(f"\nSeu dinheiro: {jogador.moedas}")
            print("0. Sair da loja")

            escolha = input("Escolha uma munição para comprar: ")

            if escolha == "0":
                break

            lista_de_municao = list(self.catalogo_municao.values())

            try:
                indice_escolha = int(escolha) - 1
                municao = lista_de_municao[indice_escolha]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                continue

            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida.")
                continue

            preco_total = municao.preco * quantidade

            if preco_total > jogador.moedas:
                print("Você não tem dinheiro suficiente.")
            else:
                jogador.moedas -= preco_total
                jogador.mochila.add_municao(municao.tipo, quantidade)
                print(f"Você comprou {quantidade}x {municao.tipo}.")