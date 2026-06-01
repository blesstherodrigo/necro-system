# textos/introducoes.py
from textos.fixar_tela import limpar_tela, enter_continuar
from audios.audio import tocar_audio
from textos.artes.artes import imprimir_arte

def introducao_jogo():
    limpar_tela()
    tocar_audio("intro.mp3")
    imprimir_arte("logo.txt")

def introducao_fase(numero_fase, nome_fase, descricao_fase):
    limpar_tela()
    print(f"=== FASE {numero_fase}: {nome_fase.upper()} ===")
    print(descricao_fase)
    enter_continuar()