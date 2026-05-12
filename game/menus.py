# game/menus.py
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def enter_voltar():
    input("\nPressione Enter para voltar...")

def enter_continuar():
    input("\nPressione Enter para continuar...")

def mostrar_menu(nome, vida, vida_max, dano, fase_atual, total_fases):
    limpar_tela()

    print("=== NECROSYSTEM ===")
    print(f"Jogador: {nome}")
    print(f"Vida: {vida}/{vida_max}")
    print(f"Dano: {dano}")
    print(f"Fase: {fase_atual}/{total_fases}")
    
    print("-" * 25)
    print("1. Explorar")
    print("2. Status")
    print("3. Mochila")
    print("4. Sair")
    print("-" * 25)

def mostrar_combate(
        nome_inimigo,
        vida_inimigo,
        vida_max_inimigo,
        vida_jogador,
        vida_max_jogador
    ):
    print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===\n")
    print(f"Sua vida: {vida_jogador}/{vida_max_jogador}")
    print(f"Vida de {nome_inimigo}: {vida_inimigo}/{vida_max_inimigo}")
    
    print("-" * 30)
    print("1. Atacar")
    print("2. Fugir")
    print("-" * 30)

def mostrar_status(jogador):
    limpar_tela()

    print("=== STATUS ===")
    print(f"Jogador: {jogador.nome}")
    print(f"Vida: {jogador.vida}/{jogador.vida_max}")
    print(f"Dano: {jogador.dano}")

    enter_voltar()

def mostrar_mochila():
    limpar_tela()

    print("=== MOCHILA ===")
    print("Mochila aqui")

    enter_voltar()