from moduloCadastramentoCartao import cadastreCliente
from modCadastramentoEstab import cadastreEstabelecimento

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


        ? - CARREGAR BANCO DE DADOS (fazer)
        0 - SAIR

        ##################################################\n
        """)
    return validaOpcao("Escolha uma opção: ", 0,2)

while True:
    opcao = menuCadastro()
    if opcao == 0:
        break
    elif opcao == 1:
        novoCartao = cadastreCliente()
        #arvoreCartoes.insere(novoCartao)
    elif opcao == 2:
        novoEstabelecimento = cadastreEstabelecimento()
        #arvoreEstabelecimentos.insere(novoEstabelecimento)
