# game/textos/fixar_tela.py
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def enter_voltar():
    input("\nPressione Enter para voltar...")

def enter_continuar():
    input("\nPressione Enter para continuar...")