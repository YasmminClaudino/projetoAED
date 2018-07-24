from objectClients import *

def cadastreClientes():
    novoCliente = Clients()
    while True:
        numeroCartao = input("Digite o número do cartão: ")
        if validaCartao(numeroCartao) == True:
            novoCliente.inserirNumero(int(numeroCartao))
            break
        else:
            print("Número do cartão é inválido, insira novamente")
    bandeiraCartao = input("Digite qual é a bandeira do cartão: ")
    novoCliente.inserirBandeira(bandeiraCartao.upper())
    nomeCliente = input("Digite o nome completo do titular: ")
    novoCliente.inserirNome(nomeCliente.upper())
    limiteTotal = float(input("Digite o limite total do cartão: "))
    novoCliente.inserirLimiteTotal(limiteTotal)
    print(novoCliente)
cadastreClientes()
