# classes/personagens/personagem.py

class Personagem:
    def __init__(self, nome, vida, vida_max, dano, imagem):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida_max
        self.dano = dano
        self.imagem = imagem

    def atacar(self, alvo):
        alvo.vida -= self.dano
        if alvo.vida < 0:
            alvo.vida = 0

    def esta_vivo(self):
        return self.vida > 0