# data/fases/hospital.py

from data.zumbis.infectados import paciente, enfermeira, doutor

zumbi_1 = paciente.paciente_infectado
zumbi_2 = enfermeira.enfermeira_infectada
boss = doutor.doutor_infectado

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