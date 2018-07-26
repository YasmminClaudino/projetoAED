from moduloCadastramentoCartao import cadastreCliente
from modCadastramentoEstab import cadastreEstabelecimento
from moduloAprovacao import analiseCompra
from arvore import *
from carregaBDs import inserirBD
from objectClients import Clients, Establishment


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

def continuar():
    input("\nPressione ENTER para continuar...")

arvore = ArvoreVP(Clients(0))
arvoreEst = ArvoreVP(Establishment(0))
while True:
    opcao = menuCadastro()
    if opcao == 0:
        break
    elif opcao == 1:
        novoCartao = cadastreCliente()
        arvore.inserir(novoCartao)
        arvore.imprimeEmOrdem(arvore.raiz)
        continuar()
    elif opcao == 2:
        novoEstabelecimento = cadastreEstabelecimento()
        arvoreEst.inserir(novoEstabelecimento)
        continuar()
    elif opcao == 3:
        print(analiseCompra(arvore, arvoreEst))
    elif opcao == 4:
        arvore = inserirBD(arvore)
        print("Foram adicionados os seguintes clientes:\n\n")
        arvore.imprimeEmOrdem(arvore.raiz)
        print("\n     ### FIM DA LISTA ###     ")
        continuar()
