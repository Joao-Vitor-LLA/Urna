from common import *

if __name__ == "__main__":
    e1 = Eleitores("Joao", 1234, 332, 78, 87)
    e2 = Eleitores("Nicolas", 4321, 789, 78, 87)
    e3 = Eleitores("Daniel", 4563, 654, 78, 87)
    c1 = Candidatos("Jair Messias", 1722, 22)
    c2 = Candidatos("Luis Inacio", 1313,13)

    eleitores = [e1, e2, e3]
    candidatos = [c1, c2]
    urna = Urna()
    urna.votar(eleitores,candidatos)
    urna.eleitores_csv(eleitores)
    urna.candidatos_csv(candidatos)