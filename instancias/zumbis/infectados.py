# instancias/zumbis/infectados.py
from classes.personagens.inimigos.zumbi import Zumbi

zumbi_infectado_1 = Zumbi(
    "Paciente Infectado",
    10, 10, 5,
    "zumbi_infectado_1.txt", "Ferro", "Cobre"
)

zumbi_infectado_2 = Zumbi(
    "Enfermeira Infectada",
    10, 10, 5,
    "zumbi_infectado_2.txt", "Ferro", "Cobre"
)

infectados = [zumbi_infectado_1, zumbi_infectado_2]