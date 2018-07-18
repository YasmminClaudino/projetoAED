class Establishment():
    def __init__(self):
        self.nome = None
        self.endereco = None
        self.horario = None
        self.montante = None
        self.valor = None
    def inserirNome(self, nome):
        self.nome = nome
    def retornaNome(self):
        return self.nome
    def inserirEndereco(self,endereco):
        self.endereco = endereco
    def inserrirHorario(self,horario):
        self.horario = horario
    def inserirMontante(self,montante):
        self.montante = montante
    def inserirValor(self,valor):
        self.valor = valor
