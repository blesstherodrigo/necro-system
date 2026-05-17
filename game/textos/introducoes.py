# game/textos/introducoes.py
from game.textos.fixar_tela import limpar_tela, enter_continuar

def introducao_fase(numero_fase, nome_fase, descricao_fase):
    limpar_tela()
    print(f"=== FASE {numero_fase}: {nome_fase.upper()} ===")
    print(descricao_fase)
    enter_continuar()