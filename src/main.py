from common import *
from tela_urna import *

if __name__ == "__main__":
    with open('src/eleitores.csv', 'r') as file:
        eleitores = [
            Eleitores(e['nome'], int(e['CPF']), int(e['titulo']), int(e['Zona']), int(e['Secao']))
            for e in csv.DictReader(file, delimiter=",")
        ]

    with open('src/candidatos.csv', 'r') as file:
        candidatos_data = list(csv.DictReader(file, delimiter=","))
        candidatos = [
            Candidatos(c['nome'], int(c['CPF']), c['numero'])
            for c in candidatos_data
        ]

    urna = Urna(eleitores, candidatos)
    cria_interface(urna, eleitores, candidatos)

