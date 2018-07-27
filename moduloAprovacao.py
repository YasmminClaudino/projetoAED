from arvore import *
from validadores import validaHorarioCompra

def analiseCompra(arvoreCartoes, arvoreEstabelecimentos):
    cardNumber = input("Informe o número do cartão: ")
    cartao = arvoreCartoes.buscar(arvoreCartoes.raiz,int(cardNumber))
    if cartao is None:
        return "Cartão não idenficado!"
    localCompra = int(input("Informe o código do estabelecimento: "))
    estabelecimento = arvoreEstabelecimentos.buscar(arvoreEstabelecimentos.raiz,localCompra)
    if estabelecimento is None:
        return "Compra negada. O estabelecimento não está cadastrado."
    horarioCompra = input("Informe o horário da compra no formato HH:MM -> ")
    if validaHorarioCompra(estabelecimento.horario.split(" - "), horarioCompra) is False:
        return "Compra negada. O estabelecimento está fechado."
    valorCompra = float(input("Valor da compra: R$ "))
    if cartao.limiteTotal >= valorCompra:
        cartao.__sub__(valorCompra)
        estabelecimento.__add__(valorCompra)
        return "\nTransação Aceita!\n\n%s\n\nNo estabelecimento:\n\n%s" %(cartao, estabelecimento)
    else:
        return "Compra negada. O valor da compra (%.2f) excede o limite disponível (%.2f)." %(valorCompra, cartao.limiteTotal)
