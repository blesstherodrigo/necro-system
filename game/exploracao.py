# game/exploracao.py

from objetos.zumbis import zumbis_fase_hospital
from game.combate import combate

def explorar(jogador):

    print("\nVocê começa a explorar...")

    print(f"Um {zumbis_fase_hospital[0].nome} apareceu!")
    resultado_do_combate = combate(jogador, zumbis_fase_hospital[0])

    if resultado_do_combate == "morreu":
        return "morreu"

    return resultado_do_combate