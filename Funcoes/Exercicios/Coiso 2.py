# Turma B
# Exercício número 2 por Juan Lucas Melo de Borba


def mult(a, b):
    if (a % b) == 0:
        print("o  numeral  {} é multiplo do numeral {}".format(a, b))
    else:
        print("o  numeral  {} não é multiplo do numeral {}".format(a, b))



a = int(input("com o dedo,  digite, pausadamente, o primeiro número. já: "))
b = int(input("agora com o orgão de sua escolha digite o segundo número: "))

mult(a, b)

