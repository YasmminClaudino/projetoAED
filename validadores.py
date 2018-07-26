def validaCartao(numeroCartao):
    if numeroCartao.isdigit():
        if 14 <= len(numeroCartao) <= 20:
            return True

def validaCodigo(codigo):
    if codigo.isdigit():
        return True

def validaHorario(entrada):
    import time
    entrada = entrada.split(" - ")
    if len(entrada) == 2:
        for horario in entrada:
            try:
                time.strptime(horario, '%H:%M')
            except ValueError:
                return False
        return "%s às %s" %(entrada[0],entrada[1])
    return False

def validaHorarioCompra(lista, C):
    A, B = lista[0], lista[1]
    #Converte em minutos
    A = (int(A[:2])*60) + int(A[3:])
    B = (int(B[:2])*60) + int(B[3:])
    C = (int(C[:2])*60) + int(C[3:])
    if A < B:
        if A <= C <= B:
            return True
    else:
        if B <= C <= A:
            return True
    return False
