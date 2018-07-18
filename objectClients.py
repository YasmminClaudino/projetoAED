class Clients():
    def __init__(self):
        self.numero = None
        self.bandeira = None
        self.nome = None
        self.limiteTotal = None
        self.limiteDisponivel = None

    def inserirNumero(self,numero):
        self.numero = numero
    def retornaNumero(self):
        return self.numero
    def inserirBandeira(self,bandeira):
        self.bandeira = bandeira
    def inserirNome(self,nome):
        self.nome = nome
    def inserirLimiteTotal(self,limiteTotal):
        self.limiteTotal = limiteTotal
    def inserirLimiteDisponivel(self,limiteDisponivel):
        self.limiteDisponivel = limiteDisponivel
