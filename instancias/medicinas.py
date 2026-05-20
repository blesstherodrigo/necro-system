# instancias/medicinas.py
from classes.itens.medicina import Medicina

adrenalina = Medicina(
    "Adrenalina",
    "buff_dano",
    5,
    20,
    "luta"
)

antidoto = Medicina(
    "Antídoto",
    "cura_instantanea",
    30,
    15,
    "instantaneo"
)

soro = Medicina(
    "Soro",
    "regeneracao",
    5,
    25,
    "luta"
)

analgesico = Medicina(
    "Analgésico",
    "buff_defesa",
    3,
    20,
    "luta"
)

medicinas = [
    adrenalina,
    antidoto,
    soro,
    analgesico
]

# | Item       |                    Efeito |       Valor |
# | ---------- | ------------------------: | ----------: |
# | Adrenalina | +5 dano até acabar a luta |       forte |
# | Antídoto   |   cura 30 de vida na hora |     simples |
# | Soro       |          cura 5 por turno | persistente |
# | Analgésico |  reduz 3 de dano recebido |   defensivo |
