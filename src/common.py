from typing import List
import csv


class Pessoa:
    nome: str
    cpf: int

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"


class Eleitores(Pessoa):
    titulo: int
    zona: int
    secao: int
    voto: bool = False

    def __init__(self, nome, cpf, titulo, zona, secao):
        super().__init__(nome, cpf)
        self.titulo = titulo
        self.zona = zona
        self.secao = secao

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Titulo: {self.titulo}, Zona: {self.zona}, Secao: {self.secao}"


class Candidatos(Pessoa):
    numero: str
    votos: int = 0

    def __init__(self, nome, cpf, numero):
        super().__init__(nome, cpf)
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Numero: {self.numero}, Votos: {self.votos}"


class Urna:
    brancos: int
    nulo: int

    def __init__(self, candidatos: List[Candidatos], brancos=0, nulo=0):
        self.nulo = nulo
        self.brancos = brancos
        self.candidatos = candidatos
    '''
    def eleitores_csv(self, eleitores: List[Eleitores], nome_arquivo='eleitores.csv'):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['nome', 'CPF', 'titulo', 'Zona', 'Secao', 'Votou'])
            for eleitor in eleitores:
                writer.writerow([eleitor.nome, eleitor.cpf, eleitor.titulo, eleitor.zona, eleitor.secao, eleitor.voto])

    def candidatos_csv(self, candidatos: List[Candidatos], nome_arquivo='candidatos.csv'):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['nome', 'CPF', 'numero'])
            for candidato in candidatos:
                writer.writerow([candidato.nome, candidato.cpf, candidato.numero])
    '''
    def urna_csv(self, candidatos: List[Candidatos], nome_arquivo='urna.csv'):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['nome', 'votos'])
            for candidato in candidatos:
                writer.writerow([candidato.nome,candidato.votos])
            writer.writerow(['Nulos', self.nulo])
            writer.writerow(['Brancos', self.brancos])

    def votar(self, eleitores: List[dict], candidatos: List[dict]):
        titulo = int(input("Digite seu titulo: "))
        eleitor = None
        candidato = None

        for e in eleitores:
            if e.titulo == titulo:
                eleitor = e
                break

        if eleitor:
            print(eleitor.nome)

            if eleitor.voto == False:
                voto = input("Digite seu voto: ")

                for c in candidatos:
                    if c.numero == voto:
                        candidato = c
                        break

                if candidato:
                    candidato.votos += 1
                    print(f"Voto registrado para {candidato.nome}.")

                elif voto == "branco":
                    print("Votou em branco")
                    self.brancos += 1

                elif not candidato:
                    self.nulo += 1
                    print("Voto anulado")

                eleitor.voto = 'True'

            else:
                print("Este eleitor já votou.")

        else:
            print("Erro: Título do eleitor não encontrado.")

    def computar(self) -> str:
        campeao = None
        max_votos = -1
        empate = False

        for candidato in self.candidatos:
            if candidato.votos > max_votos:
                max_votos = candidato.votos
                campeao = candidato
                empate = False
            elif candidato.votos == max_votos:
                empate = True

        return campeao.nome if campeao and not empate else "Nenhum vencedor"
