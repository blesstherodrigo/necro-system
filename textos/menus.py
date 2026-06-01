# textos/menus.py
from textos.fixar_tela import limpar_tela, enter_voltar

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
        print(f"{nome}: {quantidade}")

    enter_voltar()

def menu_combate(nome_inimigo, vida_inimigo, vida_max_inimigo, vida_jogador, vida_max_jogador):
    limpar_tela()
    print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===\n")
    print(f"Sua vida: {vida_jogador}/{vida_max_jogador}")
    print(f"{nome_inimigo}: {vida_inimigo}/{vida_max_inimigo}")
    print("-" * 30)
    print("1. Atacar com arma")
    print("2. Atacar com faca")
    print("3. Usar medicina")
    print("4. Fugir")
    print("-" * 30)
    opcao_combate = input("> ")
    return opcao_combate