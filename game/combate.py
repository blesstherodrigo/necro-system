# game/combate.py

def combate(jogador, inimigo):
    print(f"\nCombate contra {inimigo.nome}!")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"\nSua vida: {jogador.vida}/{jogador.vida_max}")
        print(f"Vida do {inimigo.nome}: {inimigo.vida}/{inimigo.vida_max}")

        print("\n1. Atacar")
        print("2. Fugir")
        escolha = input("> ")

        if escolha == "1":
            jogador.atacar(inimigo)

            if inimigo.esta_vivo():
                inimigo.atacar(jogador)

        elif escolha == "2":
            print("Você fugiu do combate.")
            return "fugiu"

        else:
            print("Opção inválida.")

    if jogador.esta_vivo():
        print(f"\nVocê derrotou {inimigo.nome}!")
        return "venceu"

    print("\nVocê morreu.")
    return "morreu"