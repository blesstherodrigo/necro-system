# textos/artes/artes.py

from pathlib import Path
from shutil import get_terminal_size
from pystyle import Colorate, Colors


def imprimir_arte(nome_arquivo):
    raiz_projeto = Path(__file__).resolve().parents[2]
    caminho = raiz_projeto / "textos" / "artes" / nome_arquivo

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:

            linhas = arquivo.readlines()

        largura_terminal = get_terminal_size().columns

        arte_centralizada = ""

        for linha in linhas:
            arte_centralizada += (
                linha.rstrip()
                .center(largura_terminal)
                + "\n"
            )

        print(
            Colorate.Color(
                Colors.green,
                arte_centralizada
            )
        )

    except FileNotFoundError:
        print(f"[Arte não encontrada: {nome_arquivo}]")