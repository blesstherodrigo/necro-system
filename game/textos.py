# game/textos.py
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def enter_voltar():
    input("\nPressione Enter para voltar...")

def enter_continuar():
    input("\nPressione Enter para continuar...")

# ...

def opcao_invalida():
    limpar_tela()
    print("Opção inválida.")
    enter_voltar()


# menu principal ...

def escolher_personagem():
    limpar_tela()
    print("[1] Homem | [2] Mulher")
    escolha_personagem = input("> ")
    return escolha_personagem

def digitar_nome_do_jogdor():
    limpar_tela()
    nome_jogador = input("Digite seu nome: ")
    return nome_jogador

def mostrar_menu(nome, vida, vida_max, dano, fase_atual, total_fases):
    limpar_tela()

    print("=== NECROSYSTEM ===")
    print(f"Jogador: {nome}")
    print(f"Vida: {vida}/{vida_max}")
    print(f"Dano: {dano}")
    print(f"Fases: {fase_atual}/{total_fases}")

    print("-" * 25)
    print("1. Explorar")
    print("2. Status")
    print("3. Mochila")
    print("4. Sair")
    print("-" * 25)

    opcao_menu = input("> ")
    return opcao_menu

def mostrar_status(nome, vida, vida_max, dano):
    limpar_tela()

    print("=== STATUS ===")
    print(f"Jogador: {nome}")
    print(f"Vida: {vida}/{vida_max}")
    print(f"Dano: {dano}")

    enter_voltar()

def mostrar_mochila():
    limpar_tela()

    print("=== MOCHILA ===")
    print("Mochila aqui")

    enter_voltar()

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

def saindo_do_jogo():
    limpar_tela()
    print("Saindo do jogo...")


# fase ...

def introducao_fase(numero_fase, nome_fase, descricao_fase):
    limpar_tela()
    print(f"=== FASE {numero_fase}: {nome_fase.upper()} ===")
    print(descricao_fase)
    enter_continuar()


# combate ...

def mostrar_combate(
        nome_inimigo,
        vida_inimigo,
        vida_max_inimigo,
        vida_jogador,
        vida_max_jogador
    ):
    limpar_tela()

    print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===\n")
    print(f"Sua vida: {vida_jogador}/{vida_max_jogador}")
    print(f"{nome_inimigo}: {vida_inimigo}/{vida_max_inimigo}")

    print("-" * 30)
    print("1. Atacar")
    print("2. Fugir")
    print("-" * 30)

    opcao_combate = input("> ")
    return opcao_combate

def recuou_do_combate():
    limpar_tela()
    print("Você recuou do combate.")
    enter_continuar()