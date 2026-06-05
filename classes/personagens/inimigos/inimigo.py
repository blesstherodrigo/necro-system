# classes/personagens/inimigos/inimigo.py
from classes.personagens.personagem import Personagem
from textos.mensagens import mensagem_recebeu_dano

class Inimigo(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem)
        self.fraqueza = fraqueza or []
        self.imune = imune or []

    def receber_dano_municao(self, municao):
        if municao.tipo in self.imune:
            dano = 0
            print(f"\n{self.nome} é imune a munição {municao.tipo}!")

        elif municao.tipo in self.fraqueza:
            dano = municao.dano_vantajoso
            print(f"\nDano crítico! Munição de {municao.tipo} é muito efetiva contra {self.nome}!")

        else:
            dano = municao.dano_base
            print(f"\nMunição {municao.tipo} causou dano normal.")

        dano_municao = self.receber_dano(dano)
        mensagem_recebeu_dano(self.nome, dano_municao)

    def receber_dano_faca(self, dano):
        dano_facada = self.receber_dano(dano)
        mensagem_recebeu_dano(self.nome, dano_facada)