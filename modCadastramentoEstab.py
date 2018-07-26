from objectEstablishment import Establishment
from validadores import validaCodigo, validaHorario

def cadastreEstabelecimento():
    novoEstabelecimento = Establishment(None)
    while True:
        codEstabelecimento = input("Informe o código do estabelecimento: ")
        if validaCodigo(codEstabelecimento) == True:
            novoEstabelecimento.setChave(int(codEstabelecimento))
            break
        else:
            print("ERRO: Digite apenas números.")
    nomeEstabelecimento = input("Digite o nome do estabelecimento: ")
    novoEstabelecimento.inserirNome(nomeEstabelecimento.upper())
    enderecoEstab = input("Endereço do estabelecimento: ")
    novoEstabelecimento.inserirEndereco(enderecoEstab)
    while True:
        horarioEstab = input("Horário de funcionamento (Ex.: 08:00 - 18:00): ")
        if validaHorario(horarioEstab) is not False:
            novoEstabelecimento.inserirHorario(horarioEstab)
            break
        else:
            print("Horário inválido!")
    print("\nEstabelecimento cadastrado!\n%s" %novoEstabelecimento)
    return novoEstabelecimento
