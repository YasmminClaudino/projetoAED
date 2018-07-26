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

        9 - CARREGAR BANCO DE DADOS (fazer)
        0 - SAIR

        ##################################################\n
        """)
    return validaOpcao("Escolha uma opção: ", 0,9)


arvore = ArvoreCartoes()
while True:
    opcao = menuCadastro()
    if opcao == 0:
        break
    elif opcao == 1:
        novoCartao = cadastreCliente()
        arvore.inserir(novoCartao)
        arvore.imprimePreOrdem(arvore.raiz)
    elif opcao == 2:
        novoEstabelecimento = cadastreEstabelecimento()
        #arvoreEstabelecimentos.insere(novoEstabelecimento)
    elif opcao == 3:
        analiseCompra()
    elif opcao == 9:
        inserirBD(arvore)
        arvore.imprimePreOrdem(arvore.raiz)
