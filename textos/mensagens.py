# textos/mensagens.py
from textos.tela import limpar_tela, passar_texto, enter_continuar, enter_voltar

def mensagem_opcao_invalida():
    passar_texto("\nOpção inválida.")
    enter_voltar()

def mensagem_digite_nome():
    passar_texto("\nDigite seu nome!")
    enter_voltar()

def mensagem_recebeu_dano(nome, dano):
    passar_texto(f"\n IMPACTO: {nome} recebeu {dano} de dano.")
    enter_continuar()

def mensagem_morreu():
    # Uma velocidade um pouco menor (0.05) dá mais drama para a morte
    passar_texto("\n VOCÊ MORREU... O sistema necro-orgânico consumiu você. ", velocidade=0.05)
    enter_continuar()

def mensagem_venceu(nome_inimigo):
    passar_texto(f"\n VITÓRIA: Você derrotou {nome_inimigo}!")
    # Se o seu jogo não dava enter_continuar aqui, mantemos sem ele para não quebrar o fluxo

def mensagem_ganhou_moedas(recompensa):
    passar_texto(f"\n SAQUE: Você vasculhou a área e encontrou {recompensa} moedas.")
    enter_continuar()

def mensagem_zerou_jogo():
    limpar_tela()
    passar_texto("Você sobreviveu a todas as fases do NecroSystem!")
    enter_continuar()

def mensagem_saindo_do_jogo():
    limpar_tela()
    passar_texto("Saindo do jogo...")

def mensagem_apareceu_inimigo(nome_inimigo):
    limpar_tela()
    passar_texto(f" AMEAÇA: {nome_inimigo} apareceu!")
    enter_continuar()

def mensagem_concluiu_fase(numero_fase, nome_fase):
    limpar_tela()
    passar_texto(f" Você concluiu a Fase {numero_fase}: {nome_fase}!")
    enter_continuar()

def mensagem_nova_fase_desbloqueada():
    limpar_tela()
    passar_texto("Uma nova fase foi desbloqueada no sistema.")
    enter_continuar()

def mensagem_sem_moedas_suficiente():
    passar_texto("Você não tem moedas suficientes.")
    enter_continuar()

def mensagem_comprou_item(quantidade, tipo):
    passar_texto(f"🛒 Você comprou {quantidade}x {tipo}.")
    enter_continuar()

def mensagem_vendeu_item(quantidade, nome, total):
    passar_texto(f" Você vendeu {quantidade}x {nome} por {total} moedas.")
    enter_continuar()

def mensagem_sem_itens():
    passar_texto("Você não tem itens para vender.")
    enter_continuar()

def mensagem_sem_quantidade():
    passar_texto("Você não tem essa quantidade no inventário.")
    enter_continuar()