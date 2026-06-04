# textos/tela.py
import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# mostra texto passando por letras
def passar_texto(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.01)
    print("")

# limpar uma parte especifica do terminal
def limpar_intervalo(linha_inicio, linha_fim):

    # apagar a partir da linhas inicial até a final final escolhida
    for linha in range(linha_inicio, linha_fim + 1):
        print(f"\033[{linha};1H", end="")
        print("\033[2K", end="")

    # mover cursor para a linha inicial
    print(f"\033[{linha_inicio};{1}H", end="")

def enter_voltar():
    input("\nPressione Enter para voltar...")

def enter_continuar():
    input("\nPressione Enter para continuar...")
