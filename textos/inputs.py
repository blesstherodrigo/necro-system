# textos/inputs.py
from textos.tela import limpar_tela, passar_texto, console

def input_escolha_personagem():

    console.print("[1] Homem | [2] Mulher", style ="green")
    escolha_personagem = console.input("[green]> [/]")
    return escolha_personagem

def input_nome_do_jogdor():
    nome_jogador = console.input("[green]\nDigite seu nome: [/]")
    return nome_jogador

def input_quantidade():
    try:
        quantidade = int(console.input("[green]Quantidade: [/]"))
        return quantidade
    except ValueError:
        return 0

def input_recomecar_jogo():
    limpar_tela()
    passar_texto("Deseja recomeçar o jogo?")
    passar_texto("[1] Sim | [2] Não")
    resposta_recomecar = console.input("[green]> [/]")
    return resposta_recomecar

def input_sair_do_jogo():
    limpar_tela()
    passar_texto("Tem certeza que deseja sair?")
    passar_texto("[1] Sim | [2] Não")
    resposta_sair = console.input("[green]> [/]")
    return resposta_sair