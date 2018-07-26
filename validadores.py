def validaHorario(entrada):
    entrada = entrada.split(" - ")
    if len(entrada) == 2:
        for horario in entrada:
            try:
                time.strptime(horario, '%H:%M')
            except ValueError:
                return False
        return "%s às %s" %(entrada[0],entrada[1])
    return False


def validaCartao(numeroCartao):
    if numeroCartao.isdigit():
        if 4 <= len(numeroCartao) <= 16:
            return True


def validaCodigo(codigo):
    if codigo.isdigit():
        return True