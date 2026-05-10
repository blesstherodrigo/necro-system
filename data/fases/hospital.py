# data/fases/hospital.py
from data.zumbis.infectados import paciente_infectado, enfermeira_infectada, doutor_infectado

zumbi_1 = paciente_infectado
zumbi_2 = enfermeira_infectada
boss = doutor_infectado

fase_hospital = {
    "numero": 1,
    "nome": "Hospital",
    "descricao": "Corredores escuros, macas quebradas e gritos ao longe.",
    "inimigos": [
        zumbi_1,
        zumbi_2,
        boss
    ]
}