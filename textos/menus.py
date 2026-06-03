# textos/menus.py
from textos.fixar_tela import limpar_tela, enter_voltar
from textos.ascii.ascii import imprimir_ascii_lado_a_lado

def menu_principal(fase_atual, total_fases):
    limpar_tela()
    print("=== NECROSYSTEM ===")
    print(f"FASES: {fase_atual}/{total_fases}")
    print("-" * 25)
    print("1. Explorar")
    print("2. Status")
    print("3. Loja")
    print("4. Mochila")
    print("5. Sair")
    print("-" * 25)
    opcao_menu = input("> ")
    return opcao_menu

def menu_status(nome, vida, vida_max, dano):
    limpar_tela()
    print("=== STATUS ===")
    print(f"Jogador: {nome}")
    print(f"Vida: {vida}/{vida_max}")
    print(f"Dano: {dano}")
    enter_voltar()

def menu_mochila(itens):
    print("\n=== Mochila ===")

    if not itens:
        print("Você não tem itens.")
        return

    for item, quantidade in itens.items():
        nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
        print(f"{nome} ({quantidade})")

    enter_voltar()

def menu_combate(nome_inimigo, vida_inimigo, vida_max_inimigo, inimigo_imagem, vida_jogador, vida_max_jogador, jogador_imagem):
    limpar_tela()
    imprimir_ascii_lado_a_lado(jogador_imagem, inimigo_imagem)
    print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===")
    print(f"Sua vida: {vida_jogador}/{vida_max_jogador}")
    print(f"{nome_inimigo}: {vida_inimigo}/{vida_max_inimigo}")
    print("-" * 30)
    print("1. Atacar com arma")
    print("2. Atacar com faca")
    print("3. Usar medicina")
    print("-" * 30)
    opcao_combate = input("> ")
    return opcao_combate