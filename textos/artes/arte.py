# textos/artes/arte.py
from pathlib import Path
from shutil import get_terminal_size
from itertools import zip_longest
from pystyle import Colorate, Colors
from textos.tela import limpar_tela

def caminho_arte(nome_arquivo):
    raiz_projeto = Path(__file__).resolve().parents[2]
    return raiz_projeto / "textos" / "artes" / nome_arquivo

def carregar_arte(nome_arquivo):
    caminho = caminho_arte(nome_arquivo)

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read().strip("\n").split("\n")

    except FileNotFoundError:
        return [f"[Arte não encontrada: {nome_arquivo}]"]

def mostrar_arte(nome_arquivo):
    limpar_tela()

    linhas = carregar_arte(nome_arquivo)
    largura_terminal = get_terminal_size().columns

    arte_centralizada = ""

    for linha in linhas:
        arte_centralizada += linha.rstrip().center(largura_terminal) + "\n"

    print(Colorate.Color(Colors.green, arte_centralizada))

def mostrar_artes_lado_a_lado(*nomes_arquivos, espaco=6):
    limpar_tela()

    artes = [carregar_arte(nome) for nome in nomes_arquivos]

    larguras = [
        max(len(linha) for linha in arte)
        for arte in artes
    ]

    linhas_finais = []

    for linhas in zip_longest(*artes, fillvalue=""):
        linha_final = ""

        for linha, largura in zip(linhas, larguras):
            linha_final += linha.rstrip().ljust(largura + espaco)

        linhas_finais.append(linha_final.rstrip())

    largura_terminal = get_terminal_size().columns

    arte_final = ""

    for linha in linhas_finais:
        arte_final += linha.center(largura_terminal) + "\n"

    print(Colorate.Color(Colors.green, arte_final))

def mostrar_barra_hp(vida, vida_max, tamanho=20):
    if vida_max <= 0:
        barra = "░" * tamanho
        return f"[{barra}] {vida}/{vida_max}"

    vida = max(0, min(vida, vida_max))

    percentual = vida / vida_max
    preenchido = int(tamanho * percentual)
    vazio = tamanho - preenchido

    barra = "█" * preenchido + "░" * vazio

    return f"[{barra}] {vida}/{vida_max}"