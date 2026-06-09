# instancias/fases.py
from classes.fase import Fase

from instancias.zumbis.infectados import infectados
from instancias.zumbis.eletricos import eletricos
from instancias.zumbis.acidos import acidos
from instancias.zumbis.radioativos import radioativos

fase_1 = Fase(
    1,
    "Hospital",
    "Antes um lugar de cura, agora respira morte. As luzes piscam em intervalos irregulares, "
    "alimentadas por um gerador fraco no subsolo. O cheiro de desinfetante se mistura ao de sangue seco. Macas estão viradas. "
    "   Portas batem sozinhas com o vento que entra pelas janelas quebradas..",
    "fase_1.txt",
    infectados
)

fase_2 = Fase(
    2,
    "Estação de Energia",
    "A antiga estação de energia é o único lugar que ainda envia sinais de atividade. "
    "Torres enferrujadas cortam o céu nublado. "
    "Cabos balançam com o vento, produzindo um zumbido constante, como se algo ainda estivesse vivo ali dentro.",
    "fase_2.txt",
    eletricos
)

fase_3 = Fase(
    3,
    "Laboratório",
    "Após seguir rastros de destruição deixados pela infestação, você chega a um misterioso laboratório abandonado tomado pelo silêncio e pela escuridão. Corredores destruídos, equipamentos espalhados e portas de     segurança danificadas tornam a exploração cada vez mais perigosa, enquanto zumbis vagam pelo complexo em busca de qualquer sinal de vida. Entre salas de pesquisa e setores esquecidos, "
    "você deve encontrar suprimentos e uma rota de fuga, "
    "mas logo percebe que os infectados que habitam o laboratório são mais agressivos e perigosos do que qualquer coisa enfrentada até agora. ",
    "fase_3.txt",
    acidos
)

fase_4 = Fase(
    4,
    "Usina Nuclear",
    "Após deixar o laboratório para trás, você chega a uma gigantesca usina nuclear que se ergue no horizonte como uma lembrança sombria de um mundo que já não existe. O local está em ruínas, com estruturas enferrujadas, luzes falhando e sons metálicos ecoando pelos corredores vazios. "
    "Entre áreas contaminadas e instalações abandonadas, zumbis deformados vagam pelas instalações, apresentando comportamentos estranhos e uma aparência muito mais assustadora do que os infectados encontrados anteriormente.",
    "fase_4.txt",
    radioativos
)

fases = [fase_1, fase_2, fase_3, fase_4]