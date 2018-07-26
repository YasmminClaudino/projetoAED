from moduloCadastramentoCartao import cadastreCliente
from modCadastramentoEstab import cadastreEstabelecimento
from moduloAprovacao import analiseCompra
from arvore import *
from carregaBDs import inserirBD


def validaOpcao(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Entrada inválida, digite um valor entre %d e %d" %(inicio, fim))

def menuCadastro():
    print("""\n
        ##################################################

        1 - CADASTRAR CARTÕES
        2 - CADASTRAR ESTABELECIMENTOS

        3 - APROVAÇÃO DE TRANSAÇÕES

        4 - CARREGAR BANCO DE DADOS
        0 - SAIR

        ##################################################\n
        """)
    return validaOpcao("Escolha uma opção: ", 0,4)


arvore = ArvoreCartoes()
arvoreEst = ArvoreEstabelecimentos()
while True:
    opcao = menuCadastro()
    if opcao == 0:
        break
    elif opcao == 1:
        novoCartao = cadastreCliente()
        arvore.inserir(novoCartao)
        arvore.imprimeEmOrdem(arvore.raiz)
    elif opcao == 2:
        novoEstabelecimento = cadastreEstabelecimento()
        arvoreEst.inserir(novoEstabelecimento)
    elif opcao == 3:
        print(analiseCompra())
    elif opcao == 4:
        arvore = inserirBD(arvore)
        arvore.imprimeEmOrdem(arvore.raiz)
