# textos/mensagens.py
from textos.tela import limpar_tela, passar_texto, enter_continuar, enter_voltar

VERDE = "\033[1;32m"
RED = "\033[1;31m"
AMARELO = "\033[1;33m"
RESET = "\033[0m"

def mensagem_opcao_invalida():
    passar_texto(f"\n{RED}Opção inválida.{RESET}")
    enter_voltar()

def mensagem_digite_nome():
    passar_texto(f"\n{VERDE}Digite seu nome!{RESET}")
    enter_voltar()

def mensagem_recebeu_dano(nome, dano):
    passar_texto(f"\n{RED} IMPACTO:{RESET} {VERDE}{nome} recebeu {dano} de dano.{RESET}")
    enter_continuar()

def mensagem_morreu():
    passar_texto(f"\n{RED} VOCÊ MORREU... O sistema necro-orgânico consumiu você. {RESET}", velocidade=0.05)
    enter_continuar()

def mensagem_venceu(nome_inimigo):
    passar_texto(f"\n{VERDE} VITÓRIA: Você derrotou {nome_inimigo}!{RESET}")

def mensagem_ganhou_moedas(recompensa):
    passar_texto(f"\n{VERDE} SAQUE: Você vasculhou a área e encontrou {AMARELO}{recompensa}{VERDE} moedas.{RESET}")
    enter_continuar()

def mensagem_zerou_jogo():
    limpar_tela()
    passar_texto(f"{VERDE}Você sobreviveu a todas as fases do NecroSystem!{RESET}")
    enter_continuar()

def mensagem_saindo_do_jogo():
    limpar_tela()
    passar_texto(f"{VERDE}Saindo do jogo...{RESET}")

def mensagem_apareceu_inimigo(nome_inimigo):
    limpar_tela()
    passar_texto(f"{RED} AMEAÇA:{RESET} {VERDE}{nome_inimigo} apareceu!{RESET}")
    enter_continuar()

def mensagem_concluiu_fase(numero_fase, nome_fase):
    limpar_tela()
    passar_texto(f"{VERDE} Você concluiu a Fase {numero_fase}: {nome_fase}!{RESET}")
    enter_continuar()

def mensagem_nova_fase_desbloqueada():
    limpar_tela()
    passar_texto(f"{VERDE}Uma nova fase foi desbloqueada no sistema.{RESET}")
    enter_continuar()

def mensagem_sem_moedas_suficiente():
    passar_texto(f"{RED}Você não tem moedas suficientes.{RESET}")
    enter_continuar()

def mensagem_comprou_item(quantidade, tipo):
    passar_texto(f"{VERDE} Você comprou {quantidade}x {tipo}.{RESET}")
    enter_continuar()

def mensagem_vendeu_item(quantidade, nome, total):
    passar_texto(f"{VERDE} Você vendeu {quantidade}x {nome} por {AMARELO}{total}{VERDE} moedas.{RESET}")
    enter_continuar()

def mensagem_sem_itens():
    passar_texto(f"{RED}Você não tem itens para vender.{RESET}")
    enter_continuar()

def mensagem_sem_quantidade():
    passar_texto(f"{RED}Você não tem essa quantidade no inventário.{RESET}")
    enter_continuar()