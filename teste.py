import random

class Ammo:
    def __init__(self, name, base_damage, critical_damage, price):
        self.name = name
        self.base_damage = base_damage
        self.critical_damage = critical_damage
        self.price = price

class Enemy:
    def __init__(self, name, hp, attack, weak_to=None, immune_to=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weak_to = weak_to or []
        self.immune_to = immune_to or []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, ammo):
        if ammo.name in self.immune_to:
            damage = 0
            print(f"{self.name} é imune a {ammo.name}!")
        elif ammo.name in self.weak_to:
            damage = ammo.critical_damage
            print(f"Dano crítico! {ammo.name} é muito efetiva contra {self.name}!")
        else:
            damage = ammo.base_damage
            print(f"{ammo.name} causou dano normal.")

        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"{self.name} recebeu {damage} de dano. Vida restante: {self.hp}")

class Inventory:
    def __init__(self):
        self.items = {}

    def add_ammo(self, ammo_name, quantity):
        if ammo_name not in self.items:
            self.items[ammo_name] = 0
        self.items[ammo_name] += quantity

    def use_ammo(self, ammo_name):
        if self.items.get(ammo_name, 0) > 0:
            self.items[ammo_name] -= 1
            return True
        return False

    def show(self):
        print("\n=== Mochila ===")
        if not self.items:
            print("Você não tem munições.")
            return

        for ammo_name, quantity in self.items.items():
            print(f"{ammo_name}: {quantity}")

class Player:
    def __init__(self):
        self.hp = 100
        self.money = 50
        self.inventory = Inventory()

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

        print(f"Você recebeu {damage} de dano. Sua vida: {self.hp}")

class Shop:
    def __init__(self, ammo_catalog):
        self.ammo_catalog = ammo_catalog

    def show_items(self):
        print("\n=== Mercadinho do Mercante ===")
        for index, ammo in enumerate(self.ammo_catalog.values(), start=1):
            print(
                f"{index}. {ammo.name} | "
                f"Dano: {ammo.base_damage} | "
                f"Crítico: {ammo.critical_damage} | "
                f"Preço: {ammo.price}"
            )

    def buy(self, player):
        while True:
            self.show_items()
            print(f"\nSeu dinheiro: {player.money}")
            print("0. Sair da loja")

            choice = input("Escolha uma munição para comprar: ")

            if choice == "0":
                break

            ammo_list = list(self.ammo_catalog.values())

            try:
                choice_index = int(choice) - 1
                ammo = ammo_list[choice_index]
            except (ValueError, IndexError):
                print("Escolha inválida.")
                continue

            try:
                quantity = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida.")
                continue

            total_price = ammo.price * quantity

            if total_price > player.money:
                print("Você não tem dinheiro suficiente.")
            else:
                player.money -= total_price
                player.inventory.adicionar_municao(ammo.name, quantity)
                print(f"Você comprou {quantity}x {ammo.name}.")

def choose_ammo(player, ammo_catalog):
    player.inventory.mostrar_mochila()

    available_ammo = [
        ammo_name
        for ammo_name, quantity in player.inventory.itens.itens()
        if quantity > 0
    ]

    if not available_ammo:
        print("Você não tem munição!")
        return None

    print("\nEscolha a munição:")
    for index, ammo_name in enumerate(available_ammo, start=1):
        quantity = player.inventory.itens[ammo_name]
        print(f"{index}. {ammo_name} ({quantity})")

    try:
        choice = int(input("> ")) - 1
        ammo_name = available_ammo[choice]
    except (ValueError, IndexError):
        print("Escolha inválida.")
        return None

    if player.inventory.usar_municao(ammo_name):
        return ammo_catalog[ammo_name]

    return None

def battle(player, enemy, ammo_catalog):
    print(f"\n=== Um {enemy.name} apareceu! ===")

    while player.is_alive() and enemy.is_alive():
        print("\n--- Seu turno ---")
        print(f"Sua vida: {player.hp}")
        print(f"Vida do inimigo: {enemy.hp}")

        print("\n1. Atacar")
        print("2. Ver mochila")
        print("3. Fugir")

        choice = input("> ")

        if choice == "1":
            ammo = choose_ammo(player, ammo_catalog)

            if ammo is None:
                continue

            enemy.take_damage(ammo)

        elif choice == "2":
            player.inventory.mostrar_mochila()
            continue

        elif choice == "3":
            print("Você fugiu da batalha!")
            return False

        else:
            print("Escolha inválida.")
            continue

        if enemy.is_alive():
            print(f"\n--- Turno de {enemy.name} ---")
            player.take_damage(enemy.attack)

    if player.is_alive():
        reward = random.randint(15, 35)
        player.money += reward
        print(f"\nVocê derrotou {enemy.name}!")
        print(f"Ganhou {reward} moedas.")
        return True
    else:
        print("\nVocê morreu...")
        return False


def main():
    ammo_catalog = {
        "Comum": Ammo("Comum", base_damage=10, critical_damage=15, price=5),
        "Incendiária": Ammo("Incendiária", base_damage=8, critical_damage=30, price=12),
        "Elétrica": Ammo("Elétrica", base_damage=7, critical_damage=35, price=14),
        "Prata": Ammo("Prata", base_damage=9, critical_damage=40, price=16),
    }

    enemies = [
        Enemy(
            name="Zumbi",
            hp=40,
            attack=8,
            weak_to=["Incendiária"],
            immune_to=[]
        ),
        Enemy(
            name="Robô",
            hp=55,
            attack=12,
            weak_to=["Elétrica"],
            immune_to=["Incendiária"]
        ),
        Enemy(
            name="Fantasma",
            hp=45,
            attack=10,
            weak_to=["Prata"],
            immune_to=["Comum"]
        ),
        Enemy(
            name="Mutante",
            hp=70,
            attack=15,
            weak_to=["Incendiária", "Elétrica"],
            immune_to=[]
        ),
    ]

    player = Player()

    # Munição inicial
    player.inventory.add_ammo("Comum", 5)

    shop = Shop(ammo_catalog)

    stage = 1

    while player.is_alive():
        print("\n======================")
        print(f"FASE {stage}")
        print("======================")
        print(f"Vida: {player.hp}")
        print(f"Dinheiro: {player.money}")

        print("\n1. Ir para a loja")
        print("2. Ver mochila")
        print("3. Entrar em combate")
        print("4. Sair do jogo")

        choice = input("> ")

        if choice == "1":
            shop.buy(player)

        elif choice == "2":
            player.inventory.show()

        elif choice == "3":
            enemy = random.choice(enemies)
            won = battle(player, enemy, ammo_catalog)

            # Recria o inimigo depois da luta, para ele voltar com vida cheia no futuro
            enemies = [
                Enemy("Zumbi", 40, 8, weak_to=["Incendiária"]),
                Enemy("Robô", 55, 12, weak_to=["Elétrica"], immune_to=["Incendiária"]),
                Enemy("Fantasma", 45, 10, weak_to=["Prata"], immune_to=["Comum"]),
                Enemy("Mutante", 70, 15, weak_to=["Incendiária", "Elétrica"]),
            ]

            if won:
                stage += 1

        elif choice == "4":
            print("Saindo do jogo...")
            break

        else:
            print("Escolha inválida.")

    print("\nFim de jogo.")


if __name__ == "__main__":
    main()