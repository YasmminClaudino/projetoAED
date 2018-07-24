def numero_valido(pergunta, inicio, fim):
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
        0 - SAIR

        ##################################################\n
        """)
    return numero_valido("Escolha uma opção: ", 0,2)

while True:
    opcao = menuCadastro()
    if opcao == 0:
        break
    elif opcao == 1:
        from moduloCadastramentoCartao import cadastreCliente
        cadastreCliente()
    elif opcao == 2:
        from modCadastramentoEstab import cadastreEstabelecimento
        cadastreEstabelecimento()
