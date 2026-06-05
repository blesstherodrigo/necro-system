# textos/movimentos.py

def movimento_ataque(nome, ataque):
    print(f"\n{nome} atacou com {ataque}!")

def movimento_defesa(nome, defesa):
    print(f"\n{nome} defendeu com {defesa}!")

def movimento_cura(nome, cura, quantidade):
    print(f"\n{nome} se curou com {cura} e aumentou {quantidade} de vida!")

def movimento_concentrar(nome, concentracao):
    print(f"\n{nome} ganhou mais força com {concentracao}!")

# arma/munição
def movimento_arma_imune(nome, municao):
    print(f"\nVocê atacou com arma, {nome} tem imunidade a munição de {municao}!")

def movimento_arma_fraqueza(nome, municao):
    print(f"\nVocê atacou com arma, {nome} tem fraqueza a munição de {municao}!")

def movimento_arma_neutro(nome, municao):
    print(f"\nVocê atacou com arma, {nome} tem neutralidade a munição de {municao}!")