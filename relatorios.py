from arvore import *

def clienteUnico(Arvore):
    arvore = Arvore
    cardNumber = input("Informe o número do cartão do cliente: ")
    cartao = arvore.buscar(arvore.raiz,int(cardNumber))
    if cartao is None:
        return "Cliente não idenficado!"
    else:
        return "\nCliente encontrado:\n\n%s" %cartao


def estabelecimentoUnico(Arvore):
    arvore = Arvore
    codigo = input("Informe o código do estabelecimento: ")
    cod = arvore.buscar(arvore.raiz,int(codigo))
    if cod is None:
        return "Estabelecimento não idenficado!"
    else:
        return "\nEstabelcimento encontrado:\n\n%s" %cod

def todosEstab(Arvore):
    print("Estabelecimentos cadastrados:\n\n")
    arvore = Arvore
    arvore.imprimeEmOrdem(arvore.raiz)

def todosCli(Arvore):
    print("Clientes cadastrados:\n\n")
    arvore = Arvore
    arvore.imprimeEmOrdem(arvore.raiz)