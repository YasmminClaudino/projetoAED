import time
class Establishment():
    def __init__(self):
        self.nome = None
        self.endereco = None
        self.horario = None
        self.montante = 0
        self.valor = 0
    def __str__(self):
        return "%s\n%s\nHorário de funcionamento: %s" %(self.nome,self.endereco,self.horario)
    def inserirNome(self, nome):
        self.nome = nome
    def retornaNome(self):
        return self.nome
    def inserirEndereco(self,endereco):
        self.endereco = endereco
    def inserirHorario(self,horario):
        self.horario = horario
    def inserirMontante(self,montante):
        self.montante = montante
    def inserirValor(self,valor):
        self.valor = valor
def validaHorario(entrada):
    entrada = entrada.split(" - ")
    if len(entrada) == 2:
        for horario in entrada:
            try:
                time.strptime(horario, '%H:%M')
            except ValueError:
                return False
        return "%s às %s" %(entrada[0],entrada[1])
    return False
