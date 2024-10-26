from common import *

if __name__ == "__main__":
    e1 = Eleitores("Joao", 123, 332, 78, 87)
    c1 = Candidatos("Bozonaro",1722,22)

    eleitores = [e1]
    candidatos = [c1]
    urna = Urna()
    urna.eleitores_csv(eleitores)
    urna.candidatos_csv(candidatos)