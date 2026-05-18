# classes/personagens/personagem.py

class Personagem:
    def __init__(self, nome, vida, vida_max, dano, imagem):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida_max
        self.dano = dano
        self.imagem = imagem

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0