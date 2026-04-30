from classes.arma import Arma

# (Herança) Faca filha de Arma
class Faca(Arma):
    def __init__(self, critico):
        self.critico = critico