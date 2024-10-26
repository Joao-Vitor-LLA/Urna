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
    numero: int
    votos: int = 0

    def __init__(self, nome, cpf, numero):
        super().__init__(nome, cpf)
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Numero: {self.numero}, Votos: {self.votos}"


class Urna:
    def eleitores_csv(self, eleitores: List[Eleitores], nome_arquivo='eleitores.csv'):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'CPF', 'Titulo', 'Zona', 'Secao','Votou'])
            for eleitor in eleitores:
                writer.writerow([eleitor.nome, eleitor.cpf, eleitor.titulo, eleitor.zona, eleitor.secao,eleitor.voto])

    def candidatos_csv(self, candidatos: List[Candidatos], nome_arquivo='candidatos.csv'):
        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'CPF', 'Numeros', 'Votos'])
            for candidato in candidatos:
                writer.writerow([candidato.nome, candidato.cpf, candidato.numero, candidato.votos])

    def votar(self, eleitores: List[Eleitores], candidatos: List[Candidatos], ):
        titulo = int(input("Digite seu titulo: "))
        eleitor = None
        candidato = None

        for e in eleitores:
            if e.titulo == titulo:
                eleitor = e
                break

        if eleitor:
            print(eleitor.nome)

            if not eleitor.voto:
                while candidato == None:
                    voto = int(input("Digite seu voto: "))

                    for c in candidatos:
                        if c.numero == voto:
                            candidato = c
                            break

                    if candidato:
                        candidato.votos += 1
                        eleitor.voto = True
                        print(f"Voto registrado para {candidato.nome}.")

                    else:
                        print("Numero invalido")

            else:
                print("Este eleitor já votou.")

        else:
            print("Erro: Título do eleitor não encontrado.")
