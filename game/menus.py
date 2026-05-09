def mostrar_menu():
    print("\n=== NECRO SYSTEM ===")
    print("1. Explorar")
    print("2. Status")
    print("3. Mochila")
    print("4. Sair")


def mostrar_status(jogador):
    print(f"\nNome: {jogador.nome}")
    print(f"Vida: {jogador.vida}/{jogador.vida_max}")
    print(f"Dano: {jogador.dano}")


def mostrar_mochila():
    print("\nMochila aqui")