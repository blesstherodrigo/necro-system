# data/fases/hospital.py

from data.zumbis.infectados.paciente import paciente_infectado
from data.zumbis.infectados.enfermeira import enfermeira_infectada
from data.zumbis.infectados.doutor import doutor_infectado

zumbi_1 = paciente_infectado
zumbi_2 = enfermeira_infectada
boss = doutor_infectado

fase_hospital = {
    "numero": 1,
    "nome": "Hospital",
    "descricao": "",
    "inimigos": [
        zumbi_1,
        zumbi_2,
        boss
    ]
}