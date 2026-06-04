# textos/introducoes.py
from textos.tela import limpar_tela, enter_continuar, passar_texto
from audios.audio import tocar_audio
from textos.artes.arte import mostrar_arte

def introducao_jogo():
    limpar_tela()
    tocar_audio("intro.mp3")
    mostrar_arte("logo.txt")
    enter_continuar()

def introducao_fase(imagem_fase, descricao_fase):
    limpar_tela()
    mostrar_arte(imagem_fase)
    passar_texto(descricao_fase)
    enter_continuar()