import time

class Establishment():
    def __init__(self, chave):
        self.chave = chave
        self.nome = None
        self.endereco = None
        self.horario = None
        self.montante = 0
        self.valor = 0
    def __str__(self):
        return "%04i - %s\n%s\nHorário de funcionamento: %s" %(self.chave, self.nome,self.endereco,self.horario)
    def __add__(self, valorCompra):
        self.montante += valorCompra
        self.valor += (valorCompra*0.02)
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
    #Para Arvore RB
    def setDado(self,dado):
        self.dado = dado
    def getChave(self):
        return self.chave
    def setChave(self,chave):
        self.chave = chave
    def getEsquerda(self):
        return self.esquerda
    def setEsquerda(self,esquerda):
        self.esquerda = esquerda
    def getDireita(self):
        return self.direita
    def setDireita(self,direita):
        self.direita = direita
    def getPai(self):
        return self.pai
    def setPai(self, pai):
        self.pai = pai
    def setCor(self, cor):
        self.cor = cor
    def getCor(self):
        return self.cor

