# scripts/jogo.py
from classes.jogo import Jogo
from data.fases import hospital, estacaoEnergia, laboratorio, usinaNuclear

def carregar():
    fases_jogo = [
        hospital.fase_hospital,
        estacaoEnergia.fase_estacao_de_energia,
        laboratorio.fase_laboratorio,
        usinaNuclear.fase_usina_nuclear
    ]

    jogo = Jogo(fases_jogo)
    jogo.iniciar()