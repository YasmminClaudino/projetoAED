from arvore import *
from objectClients import *

listEstablisment = []

#Abrindo Arquivos
def inserirBDEstablisments(ArvoreEst):
    listEstabs = []
    db_estabs = open("BD_Establisments.txt", "r")
    for linha in db_estabs.readlines():
        estab = linha.split("@")
        estab[3] = estab[3][:-1] #Remove o \n
        listEstabs.append(estab)
    db_estabs.close()
    arvore = ArvoreEst
    for estabelecimento in listEstabs:
        novoEstabelecimento = Establishment(int(estabelecimento[0]))
        novoEstabelecimento.inserirNome(estabelecimento[1].upper())
        novoEstabelecimento.inserirEndereco(estabelecimento[2])
        novoEstabelecimento.inserirHorario(estabelecimento[3])
        arvore.inserir(novoEstabelecimento)
    return arvore


#Fechando Arquivos
#db_estabs.close()

def inserirBDCards(Arvore):
    listCards = []
    db_cards = open("BD_Cards.txt", "r")
    for linha in db_cards.readlines():
        card = linha.split("@")
        card[3] = card[3][:-1] #Remove o \n
        listCards.append(card)
    db_cards.close()
    #arvore = ArvoreVP(Clients(0))
    arvore = Arvore
    for cartao in listCards:
        novoCliente = Clients(int(cartao[0]))
        novoCliente.inserirBandeira(cartao[1].upper())
        novoCliente.inserirNome(cartao[2].upper())
        novoCliente.inserirLimiteTotal(float(cartao[3]))
        arvore.inserir(novoCliente)
    return arvore
