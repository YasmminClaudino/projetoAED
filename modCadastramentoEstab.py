from objectEstablishment import *

def cadastreEstabelecimento():
    novoEstabelecimento = Establishment()
    nomeEstabelecimento = input("Digite o nome do estabelecimento: ")
    novoEstabelecimento.inserirNome(nomeEstabelecimento.upper())
    enderecoEstab = input("Endereço do estabelecimento: ")
    novoEstabelecimento.inserirEndereco(enderecoEstab.upper())
    while True:
        horarioEstab = input("Horário de funcionamento (Ex.: 08:00 - 18:00): ")
        if validaHorario(horarioEstab) is not False:
            novoEstabelecimento.inserirHorario(horarioEstab)
            break
        else:
            print("Horário inválido!")
    print(novoEstabelecimento)

cadastreEstabelecimento()
