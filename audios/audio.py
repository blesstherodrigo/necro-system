# audios/audio.py
from pathlib import Path
import pygame

pygame.mixer.init()

def tocar_audio(nome_arquivo):
    raiz_projeto = Path(__file__).resolve().parents[1]
    caminho = (raiz_projeto / "audios" / nome_arquivo)

    pygame.mixer.music.load(str(caminho))
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)