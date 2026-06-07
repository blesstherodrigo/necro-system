# textos/tela.py
import os
import time
import sys
from rich.console import Console

console = Console()
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# mostra texto passando por letras
def passar_texto(texto, velocidade =0.02,end="\n"):
    texto_verde = f"[green]{texto}[/]"
    with console.capture() as capture:
        console.print(texto_verde, end="")
    texto_renderizado = capture.get()

    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print(end=end, flush=True)

# limpar uma parte especifica do terminal
def limpar_intervalo(linha_inicio, linha_fim):

    # apagar a partir da linhas inicial até a final final escolhida
    for linha in range(linha_inicio, linha_fim + 1):
        passar_texto(f"\033[{linha};1H", end="")
        passar_texto("\033[2K", end="")

    # mover cursor para a linha inicial
    passar_texto(f"\033[{linha_inicio};{1}H", end="")

def enter_voltar():
    console.print("\nPressione Enter para voltar...", style="green", end="")
    console.input()

def enter_continuar():
    console.print("\nPressione Enter para continuar...", style="green", end="")
    console.input()