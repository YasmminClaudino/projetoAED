class Clients():
    def __init__(self):
        self.numero = None
        self.bandeira = None
        self.nome = None
        self.limiteTotal = None
        self.limiteDisponivel = self.limiteTotal
    def __str__(self):
        return "%s\nCartão %s\n%i\nLimite Total: R$ %.2f" %(self.nome,self.bandeira,self.numero,self.limiteTotal)

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

def validaCartao(numeroCartao):
    if numeroCartao.isdigit():
        if 14 <= len(numeroCartao) <= 16:
            return True
