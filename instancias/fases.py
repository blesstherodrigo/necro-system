# instancias/fases.py
from classes.fase import Fase

from instancias.zumbis.infectados import infectados
from instancias.zumbis.eletricos import eletricos
from instancias.zumbis.acidos import acidos
from instancias.zumbis.radioativos import radioativos

fase_1 = Fase(
    1,
    "Hospital",
    "Corredores escuros, macas quebradas e gritos ao longe.",
    "fase_1.txt",
    infectados
)

fase_2 = Fase(
    2,
    "Estação de Energia",
    "colocar uma descrição",    # colocar em arquivos .txt e importar ???
    "fase_2.txt",
    eletricos
)

fase_3 = Fase(
    3,
    "Laboratório",
    "colocar uma descrição",
    "fase_3.txt",
    acidos
)

fase_4 = Fase(
    4,
    "Usina Nuclear",
    "colocar uma descrição",
    "fase_4.txt",
    radioativos
)

fases = [fase_1, fase_2, fase_3, fase_4]