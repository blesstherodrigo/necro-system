# classes/personagens/inimigos/inimigo.py
from classes.personagens.personagem import Personagem
from textos.mensagens import mensagem_recebeu_dano
from textos.movimentos import movimento_arma_imune, movimento_arma_fraqueza, movimento_arma_neutro

class Inimigo(Personagem):
    def __init__(self, nome, vida, vida_max, dano, imagem, movimentos, fraqueza=None, imune=None):
        super().__init__(nome, vida, vida_max, dano, imagem)
        self.movimentos = movimentos
        self.fraqueza = fraqueza or []
        self.imune = imune or []

    def receber_dano_municao(self, municao):
        if municao.tipo in self.imune:
            dano = 0
            movimento_arma_imune(self.nome, municao.tipo)

        elif municao.tipo in self.fraqueza:
            dano = municao.dano_vantajoso
            movimento_arma_fraqueza(self.nome, municao.tipo)

        else:
            dano = municao.dano_base
            movimento_arma_neutro(self.nome, municao.tipo)

        dano_municao = self.receber_dano(dano)
        mensagem_recebeu_dano(self.nome, dano_municao)

    def receber_dano_faca(self, dano):
        dano_facada = self.receber_dano(dano)
        mensagem_recebeu_dano(self.nome, dano_facada)