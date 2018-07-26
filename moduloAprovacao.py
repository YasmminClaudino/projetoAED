from arvore import *

def analiseCompra():
    arvoreEstab = ArvoreEstabelecimentos()
    arvoreCart = ArvoreCartoes()
    cardNumber = input("Informe o número do cartão: ")
    localCompra = input("Informe o nome do estabelecimento: ")
    valorCompra = input("Valor da compra: R$ ")
    estabelecimento = arvoreEstab.buscar(arvoreEstab.self,int(localCompra))
    if estabelecimento is None:
        return "Compra negada. O estabelecimento não está cadastrado"
    cartao = arvoreCart.buscar(arvoreCart.raiz,int(cardNumber))
    if cartao is None:
        return "Cartão não idenficado!"
    if cartao.limiteTotal() <= valorCompra:
        cartao.__sub__(valorCompra)
        estabelecimento.__add__(valorCompra)
        return "Transação Aceita!\n",cartao
    else:
        return "Compra negada. O valor da compra (%.2f) excede o limite disponível (%.2f)" %(valorCompra, cartao.limiteTotal())
