class Pessoa():
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

    def __init__(self, titulo, zona, secao, nome, cpf):
        super().__init__(nome, cpf)
        self.titulo = titulo
        self.zona = zona
        self.secao = secao

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Titulo: {self.titulo}, Zona: {self.zona}, Secao: {self.secao}"


class Candidatos(Pessoa):
    numero : int
    votos : int = 0

    def __init__(self,nome,cpf,numero):
        super().__init__(nome, cpf)
        self.numero = numero

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Numero: {self.numero}, Votos: {self.votos}"