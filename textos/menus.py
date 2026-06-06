# textos/menus.py
from textos.tela import limpar_tela, enter_voltar, limpar_intervalo
from textos.artes.arte import mostrar_artes_lado_a_lado, mostrar_barra_hp

def menu_principal(fase_atual, total_fases):
    limpar_tela()
    print("=== NECROSYSTEM ===")
    print(f"FASES: {fase_atual}/{total_fases}")
    print("-" * 25)
    print("1. Explorar")
    print("2. Status")
    print("3. Loja")
    print("4. Mochila")
    print("5. Sair")
    print("-" * 25)
    opcao_menu = input("> ")
    return opcao_menu

def menu_status(nome, vida, vida_max, dano):
    limpar_tela()
    print("=== STATUS ===")
    print(f"Jogador: {nome}")
    print(f"Vida: {vida}/{vida_max}")
    print(f"Dano: {dano}")
    enter_voltar()

def menu_mochila(itens):
    limpar_tela()
    print("=== MOCHILA ===")
    if not itens:
        print("Você não tem itens.")
        return
    for item, quantidade in itens.items():
        nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
        print(f"{nome} ({quantidade})")
    enter_voltar()

def menu_combate(
    nome_jogador,
    nome_inimigo,
    vida_inimigo,
    vida_max_inimigo,
    inimigo_imagem,
    vida_jogador,
    vida_max_jogador,
    jogador_imagem
):
    limpar_tela()
    mostrar_artes_lado_a_lado(jogador_imagem, inimigo_imagem)
    largura_nome = max(len(nome_jogador), len(nome_inimigo))
    print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===")
    print(f"{nome_jogador:<{largura_nome}} | {mostrar_barra_hp(vida_jogador, vida_max_jogador)}")
    print(f"{nome_inimigo:<{largura_nome}} | {mostrar_barra_hp(vida_inimigo, vida_max_inimigo)}")
    print("-" * 30)
    print("1. Atacar com arma")
    print("2. Atacar com faca")
    print("3. Usar medicina")
    print("-" * 30)
    opcao_combate = input("> ")
    limpar_intervalo(40, 49)    # o menu começa na linha 40 e termina na linha 49 do terminal
    return opcao_combate

def menu_loja(moedas):
    limpar_tela()
    print("=== LOJA ===")
    print(f"Moedas: {moedas}")
    print("-" * 25)
    print("1. Comprar")
    print("2. Vender")
    print("0. Voltar")
    print("-" * 25)
    escolha = int(input("> "))
    return escolha

def menu_loja_comprar(moedas, catalogo_municao, catalogo_medicina):
    limpar_tela()
    print("=== COMPRAR ===")
    print(f"Moedas: {moedas}")
    print("-" * 80)
    print("Muniçoes:")
    largura_tipo = max(len(municao.tipo) for municao in catalogo_municao)
    largura_dano = max(len(str(municao.dano_base)) for municao in catalogo_municao)
    largura_critico = max(len(str(municao.dano_vantajoso)) for municao in catalogo_municao)
    largura_efetividade = max(len(str(municao.efetividade)) for municao in catalogo_municao)
    largura_preco = max(len(str(municao.preco)) for municao in catalogo_municao)
    for indice, municao in enumerate(catalogo_municao, start=1):
        print(
            f"{indice}. "
            f"{municao.tipo:<{largura_tipo}} | "
            f"Dano: {str(municao.dano_base):>{largura_dano}} | "
            f"Crítico: {str(municao.dano_vantajoso):>{largura_critico}} | "
            f"Efetividade: {str(municao.efetividade):<{largura_efetividade}} | "
            f"Preço: {str(municao.preco):>{largura_preco}}"
        )
    print()
    print("Medicinas:")
    largura_nome = max(len(medicina.nome) for medicina in catalogo_medicina)
    largura_efeito = max(len(medicina.efeito) for medicina in catalogo_medicina)
    largura_bonus = max(len(str(medicina.bonus)) for medicina in catalogo_medicina)
    largura_preco = max(len(str(medicina.preco)) for medicina in catalogo_medicina)
    for indice, medicina in enumerate(catalogo_medicina, start=6):
        print(
            f"{indice}. "
            f"{medicina.nome:<{largura_nome}} | "
            f"Efeito: {medicina.efeito:<{largura_efeito}} | "
            f"Bônus: {str(medicina.bonus):>{largura_bonus}} | "
            f"Preço: {str(medicina.preco):>{largura_preco}}"
        )
    print("-" * 80)
    print("0. Voltar")
    try:
        escolha = int(input("Escolha um item: "))
        return escolha
    except ValueError:
        return None

def menu_loja_vender(moedas, itens_disponiveis, itens):
    limpar_tela()
    print("=== VENDER ===")
    print(f"Moedas: {moedas}")
    print("-" * 50)
    largura_indice = len(str(len(itens_disponiveis)))
    largura_nome = max(len(getattr(item, "tipo", getattr(item, "nome", "Item"))) for item in itens_disponiveis)
    largura_quantidade = max(len(str(itens[item])) for item in itens_disponiveis)
    largura_preco_venda = max(len(str(getattr(item, "preco", 0) // 2)) for item in itens_disponiveis)
    for indice, item in enumerate(itens_disponiveis, start=1):
        quantidade = itens[item]
        nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
        preco = getattr(item, "preco", 0)
        preco_venda = preco // 2
        print(
            f"{indice:>{largura_indice}}. "
            f"{nome:<{largura_nome}} | "
            f"Qtd: {quantidade:>{largura_quantidade}} | "
            f"Venda: {preco_venda:>{largura_preco_venda}} moedas"
        )
    print("0. Voltar")
    print("-" * 50)
    try:
        escolha = int(input("Escolha um item: "))
        return escolha
    except ValueError:
        return None