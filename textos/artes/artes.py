# textos/artes/artes.py
from pathlib import Path

def imprimir_arte(nome_arquivo):
    raiz_projeto = Path(__file__).resolve().parents[2]
    caminho = raiz_projeto / "textos" / "artes" / nome_arquivo

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print(f"[Arte não encontrada: {nome_arquivo}]")