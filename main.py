from moduloCadastramentoCartao import cadastreCliente
from modCadastramentoEstab import cadastreEstabelecimento
from moduloAprovacao import analiseCompra
from arvore import *
from carregaBDs import *
from objectClients import Clients, Establishment
from relatorios import *



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
        5 - GERAR RELATÓRIOS
        0 - SAIR

        ##################################################\n
        """)
    return validaOpcao("Escolha uma opção: ", 0,5)

def menuRelatorio():
    print("""\n
        ##################################################

        1 - RELATÓRIO DE UM CLIENTE ESPECÍFICO
        2 - RELATÓRIO DE TODOS OS CLIENTES

        3 - RELATÓRIO DE UM ESTEBELECIMENTO ESPECÍFICO
        4 - RELATÓRIO DE TODOS OS ESTABELECIMENTOS
        0 - VOLTAR AO MENU PRINCIPAL

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
        continuar()
    elif opcao == 2:
        novoEstabelecimento = cadastreEstabelecimento()
        arvoreEst.inserir(novoEstabelecimento)
        continuar()
    elif opcao == 3:
        print(analiseCompra(arvore, arvoreEst))
        continuar()
    elif opcao == 4:
        arvore = inserirBDCards(arvore)
        print("Foram adicionados os seguintes clientes:\n\n")
        arvore.imprimeEmOrdem(arvore.raiz)
        print("\n     ### FIM DA LISTA ###     ")
        arvoreEst = inserirBDEstablisments(arvoreEst)
        print("Foram adicionados os seguintes estabelecimentos:\n\n")
        arvoreEst.imprimeEmOrdem(arvoreEst.raiz)
        print("\n     ### FIM DA LISTA ###     ")
        continuar()
    elif opcao == 5:
        while True:
            entrada = menuRelatorio()
            if entrada == 0:
                break
            elif entrada == 1:
                print(clienteUnico(arvore))
            elif entrada == 2:
                todosCli(arvore)
                continuar()
            elif entrada == 3:
                print(estabelecimentoUnico(arvoreEst))
            elif entrada == 4:
                todosEstab(arvoreEst)
                continuar()
