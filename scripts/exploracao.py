# scripts/exploracao.py

from data.zumbis import criar_fases
from scripts.combate import combate

fases = criar_fases()
fase_atual = 0

def explorar(jogador):
    global fase_atual

    if fase_atual >= len(fases):
        print("\nVocê já concluiu todas as fases disponíveis!")
        return "finalizado"

    fase = fases[fase_atual]

    print(f"\n=== FASE {fase['numero']}: {fase['nome'].upper()} ===")
    print(fase["descricao"])

    for inimigo in fase["inimigos"]:
        print(f"\nUm {inimigo.nome} apareceu!")
        resultado_do_combate = combate(jogador, inimigo)

        if resultado_do_combate == "morreu":
            return "morreu"

        if resultado_do_combate == "fugiu":
            print("\nVocê recuou. A fase continuará daqui quando explorar novamente.")
            return "fugiu"

    print(f"\nVocê concluiu a Fase {fase['numero']}: {fase['nome']}!")
    fase_atual += 1

    if fase_atual >= len(fases):
        print("\nParabéns! Você sobreviveu a todas as fases do NecroSystem!")
        return "finalizado"

    print("\nUma nova área foi desbloqueada.")
    return "venceu"
