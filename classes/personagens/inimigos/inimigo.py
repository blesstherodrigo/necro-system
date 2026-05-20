# classes/personagens/inimigos/inimigo.py
from classes.personagens.personagem import Personagem
from textos.fixar_tela import enter_continuar, limpar_tela

class Inimigo(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem)
        self.fraqueza = fraqueza or []
        self.imune = imune or []

    def receber_dano(self, municao):
        if municao is None:
            print("Nenhuma munição válida foi escolhida.")
            return

        if municao.tipo in self.imune:
            dano_recebido = 0
            print(f"{self.nome} é imune a munição {municao.tipo}!")
        elif municao.tipo in self.fraqueza:
            dano_recebido = municao.dano_vantajoso
            print(f"Dano crítico! Munição {municao.tipo} é muito efetiva contra {self.nome}!")
        else:
            dano_recebido = municao.dano_base
            print(f"Munição {municao.tipo} causou dano normal.")

        super().receber_dano(dano_recebido)
        print(f"\n{self.nome} recebeu {dano_recebido} de dano. Vida restante: {self.vida}")
        enter_continuar()

    def receber_dano_bruto(self, dano):
        super().receber_dano(dano)
        print(f"\n{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")
        enter_continuar()