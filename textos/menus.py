# textos/menus.py
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from textos.tela import limpar_tela, enter_voltar, limpar_intervalo, passar_texto
from textos.artes.arte import mostrar_artes_lado_a_lado, mostrar_barra_hp
from rich.table import Table

console = Console()


def menu_principal(fase_atual, total_fases):
    console.clear()
    texto_menu = (
        f"Fase Atual: {fase_atual + 1}/{total_fases}\n\n"
        "1. 🧭 Explorar Próxima Área\n"
        "2. 📊 Ver Status do Personagem\n"
        "3. 🛒 Visitar a Loja\n"
        "4. 🎒 Abrir Mochila\n"
        "5. 🚪 Sair do Jogo"
    )
    console.print(Panel(texto_menu, title="[bold white]🧟 NECRO-SYSTEM 🧟[/]", border_style="green", style="green"))
    return console.input("\nEscolha uma opção: ")


def menu_status(nome, vida, vida_max, dano):
    limpar_tela()
    passar_texto("=== STATUS ===")
    passar_texto(f"Jogador: {nome}")
    passar_texto(f"Vida: {vida}/{vida_max}")
    passar_texto(f"Dano: {dano}")
    enter_voltar()


def menu_mochila(itens):
    limpar_tela()
    passar_texto("=== MOCHILA ===")
    if not itens:
        passar_texto("Você não tem itens.")
        return
    for item, quantidade in itens.items():
        nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
        passar_texto(f"{nome} ({quantidade})")
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

    status_jogador = f"{nome_jogador} | {mostrar_barra_hp(vida_jogador, vida_max_jogador)}"
    status_inimigo = f"{nome_inimigo} | {mostrar_barra_hp(vida_inimigo, vida_max_inimigo)}"

    tabela_vida = Table(show_header=False, box=None, padding=0, width= 130)
    tabela_vida.add_column(justify="left")
    tabela_vida.add_column(justify="right")

    tabela_vida.add_row(f"[green]{status_jogador}[/]", f"[green]{status_inimigo}[/]")

    console.print(tabela_vida, justify="center")
    print()

    console.print(f"=== COMBATE CONTRA {nome_inimigo.upper()} ===", style="green", justify="center")
    print()

    bota_arma = Panel("1. 🔫 Atacar com arma", border_style="green", style="green", width=31)
    bota_faca = Panel("2. 🔪 Atacar com faca", border_style="green", style="green", width=31)
    bota_medi = Panel("3. 🩹 Usar medicina", border_style="green", style="green", width=31)

    console.print(Columns([bota_arma, bota_faca, bota_medi]), justify="center")

    opcao_combate = console.input("\n[green]> [/]")
    limpar_intervalo(40, 49)
    return opcao_combate

def menu_loja(moedas):
    limpar_tela()
    passar_texto("=== LOJA ===")
    passar_texto(f"Moedas: {moedas}")
    passar_texto("-" * 25)
    passar_texto("1. Comprar")
    passar_texto("2. Vender")
    passar_texto("0. Voltar")
    passar_texto("-" * 25)
    try:
        escolha = int(console.input("> "))
        return escolha
    except ValueError:
        return -1


def menu_loja_comprar(moedas, catalogo_municao, catalogo_medicina):
    limpar_tela()
    passar_texto("=== COMPRAR ===")
    passar_texto(f"Moedas: {moedas}")
    passar_texto("-" * 80)
    passar_texto("Munições:")
    largura_tipo = max(len(municao.tipo) for municao in catalogo_municao)
    largura_dano = max(len(str(municao.dano_base)) for municao in catalogo_municao)
    largura_critico = max(len(str(municao.dano_vantajoso)) for municao in catalogo_municao)
    largura_efetividade = max(len(str(municao.efetividade)) for municao in catalogo_municao)
    largura_preco = max(len(str(municao.preco)) for municao in catalogo_municao)
    for indice, municao in enumerate(catalogo_municao, start=1):
        passar_texto(
            f"{indice}. "
            f"{municao.tipo:<{largura_tipo}} | "
            f"Dano: {str(municao.dano_base):>{largura_dano}} | "
            f"Crítico: {str(municao.dano_vantajoso):>{largura_critico}} | "
            f"Efetividade: {str(municao.efetividade):<{largura_efetividade}} | "
            f"Preço: {str(municao.preco):>{largura_preco}}"
        )
    print()
    passar_texto("Medicinas:")
    largura_nome = max(len(medicina.nome) for medicina in catalogo_medicina)
    largura_efeito = max(len(medicina.efeito) for medicina in catalogo_medicina)
    largura_bonus = max(len(str(medicina.bonus)) for medicina in catalogo_medicina)
    largura_preco = max(len(str(medicina.preco)) for medicina in catalogo_medicina)
    for indice, medicina in enumerate(catalogo_medicina, start=6):
        passar_texto(
            f"{indice}. "
            f"{medicina.nome:<{largura_nome}} | "
            f"Efeito: {medicina.efeito:<{largura_efeito}} | "
            f"Bônus: {str(medicina.bonus):>{largura_bonus}} | "
            f"Preço: {str(medicina.preco):>{largura_preco}}"
        )
    passar_texto("0. Voltar")
    passar_texto("-" * 80)
    try:
        escolha = int(console.input("Escolha um item: "))
        return escolha
    except ValueError:
        return None


def menu_loja_vender(moedas, itens_disponiveis, itens):
    limpar_tela()
    passar_texto("=== VENDER ===")
    passar_texto(f"Moedas: {moedas}")
    passar_texto("-" * 50)
    largura_indice = len(str(len(itens_disponiveis)))
    largura_nome = max(len(getattr(item, "tipo", getattr(item, "nome", "Item"))) for item in itens_disponiveis)
    largura_quantidade = max(len(str(itens[item])) for item in itens_disponiveis)
    largura_preco_venda = max(len(str(getattr(item, "preco", 0) // 2)) for item in itens_disponiveis)
    for indice, item in enumerate(itens_disponiveis, start=1):
        quantidade = itens[item]
        nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
        preco = getattr(item, "preco", 0)
        preco_venda = preco // 2
        passar_texto(
            f"{indice:>{largura_indice}}. "
            f"{nome:<{largura_nome}} | "
            f"Qtd: {quantidade:>{largura_quantidade}} | "
            f"Venda: {preco_venda:>{largura_preco_venda}} moedas"
        )
    passar_texto("0. Voltar")
    passar_texto("-" * 50)
    try:
        escolha = int(console.input("Escolha um item: "))
        return escolha
    except ValueError:
        return None


def menu_escolher_municao(municao, itens):
    for indice, municao in enumerate(municao, start=1):
        quantidade = itens[municao]
        passar_texto(f"{indice}. {municao.tipo} ({quantidade})")
    passar_texto("0. Voltar")
    passar_texto("-" * 25)
    passar_texto("Escolha a munição:")
    try:
        escolha = int(console.input("> "))
        return escolha
    except ValueError:
        return 0


def menu_escolher_medicina(medicina, itens):
    for indice, medicina in enumerate(medicina, start=1):
        quantidade = itens[medicina]
        passar_texto(
            f"{indice}. {medicina.nome} "
            f"({quantidade}) | Efeito: {medicina.efeito} | Bônus: {medicina.bonus}"
        )
    passar_texto("0. Voltar")
    passar_texto("-" * 25)
    passar_texto("Escolha a medicina:")
    try:
        escolha = int(console.input("> "))
        return escolha
    except ValueError:
        return 0