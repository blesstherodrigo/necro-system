# game/carregarJogo.py
from classes.jogo import Jogo
from data.fases import estacao_energia, hospital, laboratorio, usina_nuclear

def carregar():
    fases_jogo = [
        hospital.fase_hospital,
        estacao_energia.fase_estacao_de_energia,
        laboratorio.fase_laboratorio,
        usina_nuclear.fase_usina_nuclear
    ]

    jogo = Jogo(fases_jogo)
    jogo.iniciar()