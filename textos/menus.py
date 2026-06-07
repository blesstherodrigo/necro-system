# textos/menus.py
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from rich.align import Align
from rich.box import ROUNDED
from rich.console import Group
from textos.tela import limpar_tela, enter_voltar, limpar_intervalo, passar_texto
from textos.artes.arte import mostrar_artes_lado_a_lado, mostrar_barra_hp

console = Console()


def menu_principal(fase_atual, total_fases):
    # Mantemos o input nativo para garantir que o retorno seja a string exata
    # que o seu classes/jogo.py precisa, mas mantendo a caixa estilizada do Rich!
    limpar_tela()
    texto_menu = (
        f"Fase Atual: {fase_atual + 1}/{total_fases}\n\n"
        "1. 🧭 Explorar Próxima Área\n"
        "2. 📊 Ver Status do Personagem\n"
        "3. 🛒 Visitar a Loja\n"
        "4. 🎒 Abrir Mochila\n"
        "5. 🚪 Sair do Jogo"
    )
    console.print(Panel(texto_menu, title="[bold white]🧟 NECRO-SYSTEM 🧟[/]", border_style="green", width=50))
    return input("\nEscolha uma opção: ")


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
    limpar_tela()
    texto_loja = (
        f"Seu Saldo: [bold yellow]{moedas} moedas[/]\n\n"
        "[bold green][1][/] Comprar Equipamentos\n"
        "[bold green][2][/] Vender Itens da Mochila\n"
        "[bold red][0][/] Voltar ao Menu Principal"
    )
    console.print(Align.center(
        Panel(texto_loja, title="[bold green]=== MERCADO NECOSYSTEM ===[/]", border_style="white", width=60,
              box=ROUNDED)))
    try:
        return int(input(f"\n{' ' * 42}Escolha uma opção: "))
    except ValueError:
        return -1


def menu_loja_comprar(moedas, catalogo_municao, catalogo_medicina):
    LARGURA_LOJA = 130
    elementos_loja = []

    # Cabeçalho interno
    elementos_loja.append(Align.center("[bold green]=== AMBIENTE DE COMPRAS ===[/]"))
    elementos_loja.append(Align.center(f"Seu Saldo: [bold yellow]{moedas} Moedas[/]\n"))

    elementos_loja.append("[bold green]📦 MUNIÇÕES[/]")

    # Renderiza cada munição com sua própria mini-borda verde
    for indice, municao in enumerate(catalogo_municao, start=1):
        tipo_alinhado = f"{municao.tipo:<12}"
        dano = getattr(municao, "dano_base", "5")
        critico = getattr(municao, "dano_vantajoso", "5")
        efetividade = getattr(municao, "efetividade", "Nenhuma")

        info_stats = f"Dano: [cyan]{dano:<2}[/] | Crítico: [cyan]{critico:<2}[/] | Efetividade: [cyan]{efetividade:<15}[/]"
        preco = f"[bold yellow]Preço: {municao.preco:<3} moedas[/]"

        linha_item = f"[bold cyan]{indice}.[/] {tipo_alinhado} ❖ {info_stats} ❖ {preco}"
        elementos_loja.append(Panel(linha_item, border_style="green", box=ROUNDED))

    elementos_loja.append("\n[bold green]🧪 MEDICINAS[/]")

    # Renderiza cada medicina com sua própria mini-borda verde
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

    # Junta tudo em uma única grande borda macro branca
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


def menu_escolher_municao(municao, itens):
    for indice, m in enumerate(municao, start=1):
        quantidade = itens[m]
        passar_texto(f"{indice}. {m.tipo} ({quantidade})")
    passar_texto("0. Voltar")
    passar_texto("-" * 25)
    passar_texto("Escolha a munição:")
    try:
        return int(input("> "))
    except ValueError:
        return 0


def menu_escolher_medicina(medicina, itens):
    for indice, m in enumerate(medicina, start=1):
        quantidade = itens[m]
        passar_texto(f"{indice}. {m.nome} ({quantidade}) | Efeito: {m.efeito} | Bônus: {m.bonus}")
    passar_texto("0. Voltar")
    passar_texto("-" * 25)
    passar_texto("Escolha a medicina:")
    try:
        return int(input("> "))
    except ValueError:
        return 0