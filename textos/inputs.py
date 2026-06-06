# textos/inputs.py
from textos.tela import limpar_tela

def input_escolha_personagem():
    print("[1] Homem | [2] Mulher")
    escolha_personagem = input("> ")
    return escolha_personagem

def input_nome_do_jogdor():
    nome_jogador = input("\nDigite seu nome: ")
    return nome_jogador

def input_quantidade():
    quantidade = int(input(f"Quantidade: "))
    return quantidade

def input_recomecar_jogo():
    limpar_tela()
    print("Deseja recomeçar o jogo?")
    print("[1] Sim | [2] Não")
    resposta_recomecar = input("> ")
    return resposta_recomecar

def input_sair_do_jogo():
    limpar_tela()
    print("Tem certeza que deseja sair?")
    print("[1] Sim | [2] Não")
    resposta_sair = input("> ")
    return resposta_sair