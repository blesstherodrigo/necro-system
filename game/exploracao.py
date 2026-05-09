from objetos.zumbis import zumbis
from game.combate import combate


def explorar(jogador):
    print("\nVocê começa a explorar...")

    print(f"Um {zumbis[0].nome} apareceu!")
    resultado = combate(jogador, zumbis[0])

    if resultado == "morreu":
        return "morreu"

    print("O lugar ficou silencioso...")
    print("Apareceu outro zumbi.")

    resultado = combate(jogador, zumbis[1])

    return resultado