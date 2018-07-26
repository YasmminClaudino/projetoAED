from arvore import *

def analiseCompra():
    from main import arvore,arvoreEst
    cardNumber = input("Informe o número do cartão: ")
    localCompra = int(input("Informe o nome do estabelecimento: "))
    valorCompra = float(input("Valor da compra: R$ "))
    cartao = arvore.buscar(arvore.raiz,int(cardNumber))
    if cartao is None:
        return "Cartão não idenficado!"
    estabelecimento = arvoreEst.buscar(arvoreEst.raiz,localCompra)
    if estabelecimento is None:
        return "Compra negada. O estabelecimento não está cadastrado"
    if cartao.limiteTotal <= valorCompra:
        cartao.__sub__(valorCompra)
        estabelecimento.__add__(valorCompra)
        return "Transação Aceita!\n",cartao
    else:
        return "Compra negada. O valor da compra (%.2f) excede o limite disponível (%.2f)" %(valorCompra, cartao.limiteTotal())
