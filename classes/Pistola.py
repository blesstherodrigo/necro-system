from classes.arma import Arma

# (Herança) classe Pistola filha de Arma
class Pistola(Arma):
    def __init__(self, municao):
        self.municao = municao