# textos/confirmacoes.py
from textos.fixar_tela import limpar_tela

def confirmacao_recomecar_jogo():
    limpar_tela()
    print("Deseja recomeçar o jogo?")
    print("[1] Sim | [2] Não")
    resposta_recomecar = input("> ")
    return resposta_recomecar

def confirmacao_sair_do_jogo():
    limpar_tela()
    print("Tem certeza que deseja sair?")
    print("[1] Sim | [2] Não")
    resposta_sair = input("> ")
    return resposta_sair