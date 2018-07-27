from main import *
from arvore import *

def clienteUnico():
    cardNumber = input("Informe o número do cartão do cliente: ")
    cartao = arvoreCartoes.buscar(arvoreCartoes.raiz,int(cardNumber))
    if cartao is None:
        return "Cliente não idenficado!"
    else:
        cliente.imprimeEmOrdem(cliente.raiz)
        return cliente

def validaOpcao(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
        except ValueError:
            print("Entrada inválida, digite um valor entre %d e %d" %(inicio, fim))

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

cliente = ArvoreVP(Clients(0))
while True:
    opcao = menuRelatorio()
    if opcao == 0:
        m = menuCadastro()
        break
    elif opcao == 1:
        c = clienteUnico()
    elif opcao == 3:
        continue
    elif opcao == 4:
        continue
