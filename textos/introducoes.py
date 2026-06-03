# textos/introducoes.py
from textos.fixar_tela import limpar_tela, enter_continuar
from audios.audio import tocar_audio
from textos.artes.arte import mostrar_arte

def introducao_jogo():
    limpar_tela()
    tocar_audio("intro.mp3")
    mostrar_arte("logo.txt")
    enter_continuar()

def introducao_fase(numero_fase, nome_fase, imagem_fase, descricao_fase):
    limpar_tela()
    print(f"=== FASE {numero_fase}: {nome_fase.upper()} ===")
    mostrar_arte(imagem_fase)
    print(descricao_fase)
    enter_continuar()