from common import *
from tela_urna import *

if __name__ == "__main__":
    with open('eleitores.csv', 'r') as file:
        eleitores = [Eleitores(e['nome'], int(e['CPF']), int(e['titulo']), int(e['Zona']), int(e['Secao']))
            for e in csv.DictReader(file, delimiter=",")]

    with open('candidatos.csv', 'r') as file:
        candidatos_data = list(csv.DictReader(file, delimiter=","))
        candidatos = [Candidatos(c['nome'], int(c['CPF']), c['numero'])
            for c in candidatos_data]

    urna = Urna(eleitores, candidatos)  # Cria a instância da urna passando eleitores e candidatos
    tela(eleitores, candidatos)  # Passa eleitores e candidatos para a função tela

