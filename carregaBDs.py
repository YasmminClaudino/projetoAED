listCards = []
listEstablisment = []

#Abrindo Arquivos
db_cards = open("BD_Cards.txt", "r")
#db_estabs = open("BD_Establisments", "r")

for linha in db_cards.readlines():
    card = linha.split("@")
    card[3] = card[3][:-1] #Remove o \n
    listCards.append(card)
"""
for linha in db_estabs.readlines():
    estab = linha.split("@")
    card[3] = card[3][:-1] #Remove o \n
    listCards.append(card)
"""
#Fechando Arquivos
db_cards.close()
#db_estabs.close()

#print(listCards)
