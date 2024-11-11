from common import *

if __name__ == "__main__":
    with open('eleitores.csv', 'r') as file:
        eleitores = [
            Eleitores(e['nome'], int(e['CPF']), int(e['titulo']), int(e['Zona']), int(e['Secao']))
            for e in csv.DictReader(file, delimiter=",")
        ]

    with open('candidatos.csv', 'r') as file:
        candidatos_data = list(csv.DictReader(file, delimiter=","))
        candidatos = [Candidatos(c['nome'], int(c['CPF']), c['numero'])
            for c in candidatos_data]
    '''
    e1 = Eleitores("Joao", 1234, 332, 78, 87)
    e2 = Eleitores("Nicolas", 4321, 789, 78, 87)
    e3 = Eleitores("Daniel", 4563, 654, 78, 87)
    c1 = Candidatos("Jair Messias", 1722, "22")
    c2 = Candidatos("Luis Inacio", 1313,"13")
    '''

    urna = Urna(candidatos)
    while any(not eleitor.voto for eleitor in eleitores):
        urna.votar(eleitores, candidatos)
    print(urna.computar() + " ganhou!")
    urna.urna_csv(candidatos)

