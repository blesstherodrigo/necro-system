from game.textos.fixar_tela import limpar_tela, enter_voltar

def menu_principal(nome, vida, vida_max, dano, fase_atual, total_fases):
    limpar_tela()
    print("=== NECROSYSTEM ===")
    print(f"Jogador: {nome}")
    print(f"Vida: {vida}/{vida_max}")
    print(f"Dano: {dano}")
    print(f"Fases: {fase_atual}/{total_fases}")
    print("-" * 25)
    print("1. Explorar")
    print("2. Status")
    print("3. Mochila")
    print("4. Sair")
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

def menu_mochila():
    limpar_tela()
    print("=== MOCHILA ===")
    print("Mochila aqui")
    enter_voltar()

def menu_combate(nome_inimigo, vida_inimigo, vida_max_inimigo, vida_jogador, vida_max_jogador):
    limpar_tela()
    print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===\n")
    print(f"Sua vida: {vida_jogador}/{vida_max_jogador}")
    print(f"{nome_inimigo}: {vida_inimigo}/{vida_max_inimigo}")
    print("-" * 30)
    print("1. Atacar")
    print("2. Fugir")
    print("-" * 30)
    opcao_combate = input("> ")
    return opcao_combate