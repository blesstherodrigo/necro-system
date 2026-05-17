# game/textos/inputs.py
from game.textos.fixar_tela import limpar_tela

def receber_escolha_personagem():
    limpar_tela()
    print("[1] Homem | [2] Mulher")
    escolha_personagem = input("> ")
    return escolha_personagem

def receber_nome_do_jogdor():
    limpar_tela()
    nome_jogador = input("Digite seu nome: ")
    return nome_jogador