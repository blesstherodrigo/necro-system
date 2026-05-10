# game/menus.py
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione Enter para continuar...")

def mostrar_menu(jogador=None, fase_atual=None, total_fases=None):
    limpar_tela()

    print("=== NECROSYSTEM ===")

    if jogador:
        print(f"Jogador: {jogador.nome}")
        print(f"Vida: {jogador.vida}/{jogador.vida_max}")
        print(f"Dano: {jogador.dano}")

    if fase_atual is not None and total_fases is not None:
        print(f"Fase: {fase_atual + 1}/{total_fases}")

    print("-" * 25)
    print("1. Explorar")
    print("2. Status")
    print("3. Mochila")
    print("4. Sair")
    print("-" * 25)

def mostrar_status(jogador):
    limpar_tela()

    print("=== STATUS ===")
    print(f"Nome: {jogador.nome}")
    print(f"Vida: {jogador.vida}/{jogador.vida_max}")
    print(f"Dano: {jogador.dano}")

    pausar()

def mostrar_mochila():
    limpar_tela()

    print("=== MOCHILA ===")
    print("Mochila aqui")

    pausar()