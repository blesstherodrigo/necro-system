# instancias/medicinas.py
from classes.itens.medicina import Medicina

adrenalina = Medicina(
    "Adrenalina",
    "+ Dano Duradouro",
    5,
    20,
    "luta"
)

antidoto = Medicina(
    "Antídoto",
    "Cura Instantânea",
    30,
    15,
    "instantaneo"
)

soro = Medicina(
    "Soro",
    "Regeneração Duradouro",
    5,
    25,
    "luta"
)

analgesico = Medicina(
    "Analgésico",
    "+ Defesa Duradouro",
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
