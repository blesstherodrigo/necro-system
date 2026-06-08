# textos/menus.py
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from rich.align import Align
from rich.box import ROUNDED
from rich.console import Group
from rich.prompt import Prompt
from textos.tela import limpar_tela, enter_voltar, limpar_intervalo, passar_texto
from textos.artes.arte import mostrar_artes_lado_a_lado, mostrar_barra_hp

VERDE = "\033[1;32m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
RESET = "\033[0m"


console = Console()


def menu_principal(fase_atual, total_fases):
    console.clear()

    status_progresso = f"[bold green]NECRO-SYSTEM[/]\n[green]Progresso: Área {fase_atual + 1}/{total_fases}[/]"
    painel_topo = Panel(status_progresso, border_style="green", expand=False)

    opt_1 = Panel("[bold green]1[/] - EXPLORAR ÁREA", border_style="green", expand=True)
    opt_2 = Panel("[bold green]2[/] - STATUS DO PERSONAGEM", border_style="green", expand=True)
    opt_3 = Panel("[bold green]3[/] - VISITAR A LOJA", border_style="green", expand=True)
    opt_4 = Panel("[bold green]4[/] - ABRIR MOCHILA", border_style="green", expand=True)
    opt_5 = Panel("[bold green]5[/] - SAIR DO JOGO", border_style="green", expand=True)

    conteudo_menu = Group(
        Align.center(painel_topo),
        "",
        Align.center(opt_1, width=40),
        Align.center(opt_2, width=40),
        Align.center(opt_3, width=40),
        Align.center(opt_4, width=40),
        Align.center(opt_5, width=40)
    )

    menu_completo = Panel(
        conteudo_menu,
        #title="[bold green]  [/]",
        border_style="green",
        expand=False
    )

    console.print("")
    console.print(Align.center(menu_completo))
    console.print("")

    console.print("[bold green]Selecione uma opção[/]")
    console.print("[bold green]> [/]", end="")

    escolha = input().strip()

    return escolha

def menu_status(nome, vida, vida_max, dano):
    console.clear()

    itens_paineis = []

    info_jogador = f"[bold green]Jogador:[/] [bold white]{nome}[/]"
    info_vida = f"[bold green]Vida:[/] [bold white]{vida}/{vida_max}[/]"
    info_dano = f"[bold green]Dano:[/] [bold white]{dano}[/]"

    itens_paineis.append(Panel(info_jogador, border_style="green", expand=True))
    itens_paineis.append(Panel(info_vida, border_style="green", expand=True))
    itens_paineis.append(Panel(info_dano, border_style="green", expand=True))

    botao_voltar = Panel("[bold red]Enter. Voltar para o menu anterior[/]", border_style="red", expand=True)
    itens_paineis.append(botao_voltar)

    conteudo_status = Group(*itens_paineis)
    painel_principal = Panel(
        conteudo_status,
        title="=== STATUS ===",
        border_style="green",
        expand=False,
        width=80
    )

    console.print("")
    console.print(Align.center(painel_principal))
    console.print("")

    console.print("[bold green]Pressione Enter para voltar...[/]")
    console.print("[bold green]> [/]", end="")
    input()


def menu_mochila(itens):
    console.clear()

    itens_paineis = []

    if not itens:
        itens_paineis.append(
            Panel("[bold red]Você não tem itens.[/]", border_style="red", expand=True)
        )
    else:
        contador = 1
        for item, quantidade in itens.items():
            nome = getattr(item, "tipo", getattr(item, "nome", "Item"))

            info_item = f"[bold cyan]{contador}.[/] {nome:<20} | [bold green]Quantidade:[/] [bold white]{quantidade}[/]"

            itens_paineis.append(
                Panel(info_item, border_style="green", expand=True)
            )
            contador += 1

    botao_voltar = Panel("[bold red]Enter. Voltar para o menu anterior[/]", border_style="red", expand=True)
    itens_paineis.append(botao_voltar)

    conteudo_mochila = Group(*itens_paineis)
    painel_principal = Panel(
        conteudo_mochila,
        title="=== MOCHILA ===",
        border_style="green",
        expand=False,
        width=80
    )

    console.print("")
    console.print(Align.center(painel_principal))
    console.print("")

    console.print("[bold green]Pressione Enter para voltar...[/]")
    console.print("[bold green]> [/]", end="")
    input()

def menu_combate(nome_jogador, nome_inimigo, vida_inimigo, vida_max_inimigo, inimigo_imagem, vida_jogador,
                 vida_max_jogador, jogador_imagem):
    limpar_tela()
    mostrar_artes_lado_a_lado(jogador_imagem, inimigo_imagem)

    status_jogador = f"{nome_jogador} | {mostrar_barra_hp(vida_jogador, vida_max_jogador)}"
    status_inimigo = f"{nome_inimigo} | {mostrar_barra_hp(vida_inimigo, vida_max_inimigo)}"

    tabela_vida = Table(show_header=False, box=None, padding=0, width=130)
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

    opcao_combate = input("\n> ")
    limpar_intervalo(40, 49)
    return opcao_combate


def menu_loja(moedas):
    console.clear()

    itens_paineis = []

    info_saldo = f"Seu Saldo: [bold yellow]{moedas} moedas[/]"
    itens_paineis.append(Panel(info_saldo, border_style="green", expand=True))

    opt_1 = "[bold cyan]1.[/] Comprar Equipamentos"
    opt_2 = "[bold cyan]2.[/] Vender Itens da Mochila"

    itens_paineis.append(Panel(opt_1, border_style="green", expand=True))
    itens_paineis.append(Panel(opt_2, border_style="green", expand=True))

    botao_voltar = Panel("[bold red]0. Voltar para o menu anterior[/]", border_style="red", expand=True)
    itens_paineis.append(botao_voltar)

    conteudo_loja = Group(*itens_paineis)
    painel_principal = Panel(
        conteudo_loja,
        title="=== MERCADO ===",
        border_style="white",
        expand=False,
        width=80
    )

    console.print("")
    console.print(Align.center(painel_principal))
    console.print("")

    console.print("[bold green]Escolha uma opção[/]")
    console.print("[bold green]> [/]", end="")

    try:
        return int(input().strip())
    except ValueError:
        return -1

def menu_loja_comprar(moedas, catalogo_municao, catalogo_medicina):
    LARGURA_LOJA = 130
    elementos_loja = []

    elementos_loja.append(Align.center("[bold green]=== LOJA ===[/]"))
    elementos_loja.append(Align.center(f"Seu Saldo: [bold yellow]{moedas} Moedas[/]\n"))

    elementos_loja.append("[bold green] MUNIÇÕES[/]")

    for indice, municao in enumerate(catalogo_municao, start=1):
        tipo_alinhado = f"{municao.tipo:<12}"
        dano = getattr(municao, "dano_base", "5")
        critico = getattr(municao, "dano_vantajoso", "5")
        efetividade = getattr(municao, "efetividade", "Nenhuma")

        info_stats = f"Dano: [cyan]{dano:<2}[/] | Crítico: [cyan]{critico:<2}[/] | Efetividade: [cyan]{efetividade:<15}[/]"
        preco = f"[bold yellow]Preço: {municao.preco:<3} moedas[/]"

        linha_item = f"[bold cyan]{indice}.[/] {tipo_alinhado} ❖ {info_stats} ❖ {preco}"
        elementos_loja.append(Panel(linha_item, border_style="green", box=ROUNDED))

    elementos_loja.append("\n[bold green] MEDICINAS[/]")

    for indice, medicina in enumerate(catalogo_medicina, start=6):
        nome_alinhado = f"{medicina.nome:<12}"
        efeito = getattr(medicina, "efeito", "Cura")
        bonus = getattr(medicina, "bonus", "0")

        info_stats = f"Efeito: [cyan]{efeito:<23}[/] | Bônus: [cyan]{bonus:<2}[/]"
        preco = f"[bold yellow]Preço: {medicina.preco:<3} moedas[/]"

        linha_item = f"[bold cyan]{indice}.[/] {nome_alinhado} ❖ {info_stats:<49} ❖ {preco}"
        elementos_loja.append(Panel(linha_item, border_style="green", box=ROUNDED))

    elementos_loja.append("")
    elementos_loja.append(Panel("[bold red]0. Voltar para o menu anterior[/]", border_style="red", box=ROUNDED))

    painel_geral = Panel(
        Group(*elementos_loja),
        border_style="white",
        box=ROUNDED,
        width=LARGURA_LOJA
    )

    limpar_tela()
    console.print(Align.center(painel_geral))

    try:
        return int(input(f"\n{' ' * 45}Escolha um item: "))
    except ValueError:
        return None


def menu_loja_vender(moedas, itens_disponiveis, itens):
    LARGURA_LOJA = 130
    elementos_loja = []

    elementos_loja.append(Align.center("[bold green]=== BALCÃO DE VENDAS ===[/]"))
    elementos_loja.append(Align.center(f"Seu Saldo: [bold yellow]{moedas} Moedas[/]\n"))
    elementos_loja.append("[bold yellow]💰 Seus itens na mochila (Valor de venda: metade do preço):[/]\n")

    for indice, item in enumerate(itens_disponiveis, start=1):
        quantidade_possuida = itens[item]
        nome = getattr(item, "tipo", getattr(item, "nome", "Item"))
        nome_alinhado = f"{nome:<20}"
        preco_venda = getattr(item, "preco", 0) // 2

        linha = f"[bold cyan]{indice}.[/] {nome_alinhado} ❖ Qtd no Inventário: [cyan]{quantidade_possuida:<3}[/] ❖ [bold yellow]Valor de Venda: {preco_venda} moedas[/]"
        elementos_loja.append(Panel(linha, border_style="green", box=ROUNDED))

    elementos_loja.append("")
    elementos_loja.append(Panel("[bold red]0. Voltar para o menu anterior[/]", border_style="red", box=ROUNDED))

    painel_geral = Panel(
        Group(*elementos_loja),
        border_style="white",
        box=ROUNDED,
        width=LARGURA_LOJA
    )

    limpar_tela()
    console.print(Align.center(painel_geral))

    try:
        return int(input(f"\n{' ' * 45}Escolha um item para vender: "))
    except ValueError:
        return None


def menu_escolher_municao(municao_disponivel, itens_mochila):
    contador = 1

    for item in municao_disponivel:
        quantidade = itens_mochila.get(item, 0)
        nome = getattr(item, "tipo", getattr(item, "nome", "Munição"))

        print(f"{VERDE}[ {VERDE}{contador}. {nome} ({quantidade}) {VERDE}]{RESET}")
        contador += 1

    print(f"{RED}[ 0. Voltar ]{RESET}")
    print(f"{VERDE}-----------------------------------------{RESET}")
    print(f"{VERDE}Escolha a munição:{RESET}")
    print(f"{VERDE}> {RESET}", end="")

    return int(input().strip())


def menu_escolher_medicina(medicinas_disponiveis, itens_mochila):
    contador = 1

    for item in medicinas_disponiveis:
        quantidade = itens_mochila.get(item, 0)
        nome = getattr(item, "tipo", getattr(item, "nome", "Medicina"))
        efeito = getattr(item, "efeito", "Cura")
        bonus = getattr(item, "bonus", 0)

        print(f"{VERDE}[ {CYAN}{contador}. {nome} ({quantidade}) | Efeito: {efeito} | Bônus: {bonus} {VERDE}]{RESET}")
        contador += 1

    print(f"{RED}[ 0. Voltar ]{RESET}")
    print(f"{VERDE}-----------------------------------------{RESET}")
    print(f"{VERDE}Escolha a medicina:{RESET}")
    print(f"{VERDE}> {RESET}", end="")

    return int(input().strip())