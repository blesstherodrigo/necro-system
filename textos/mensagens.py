# textos/mensagens.py
from textos.fixar_tela import limpar_tela, enter_continuar, enter_voltar

def mensagem_opcao_invalida():
    limpar_tela()
    print("Opção inválida.")
    enter_voltar()

def mensagem_recebeu_dano(nome, dano):
    print(f"\n{nome} recebeu {dano} de dano.")

def mensagem_recuou():
    limpar_tela()
    print("Você recuou do combate.")
    enter_continuar()

def mensagem_morreu():
    print("\nVocê morreu.")
    enter_continuar()

def mensagem_venceu(nome_inimigo):
    print(f"\nVocê derrotou {nome_inimigo}!")
    enter_continuar()

def mensagem_ganhou_moedas(recompensa):
    print(f"\nGanhou {recompensa} moedas.")
    enter_continuar()

def mensagem_zerou_jogo():
    limpar_tela()
    print("Você sobreviveu todas as fases do NecroSystem!")
    enter_continuar()

def mensagem_saindo_do_jogo():
    limpar_tela()
    print("Saindo do jogo...")

def mensagem_apareceu_inimigo(nome_inimigo):
    limpar_tela()
    print(f"Um {nome_inimigo} apareceu!")
    enter_continuar()

def mensagem_concluiu_fase(numero_fase, nome_fase):
    limpar_tela()
    print(f"Você concluiu a Fase {numero_fase}: {nome_fase}!")
    enter_continuar()

def mensagem_nova_fase_desbloqueada():
    limpar_tela()
    print("Uma nova fase foi desbloqueada.")
    enter_continuar()