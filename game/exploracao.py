# game/exploracao.py

from objetos.zumbis import zumbis_fase_hospital
from game.combate import combate

def explorar(jogador):
    print("\nVocê começa a explorar...")

    print(f"Um {zumbis_fase_hospital[0].nome} apareceu!")
    resultado = combate(jogador, zumbis_fase_hospital[0])

    if resultado == "morreu":
        return "morreu"

    print("O lugar ficou silencioso...")
    print("Apareceu outro zumbi.")

    resultado = combate(jogador, zumbis_fase_hospital[1])

    return resultado