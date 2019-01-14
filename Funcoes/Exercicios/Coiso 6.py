# Turma B
# Exercício número 6 por Juan Lucas Melo de Borba


def frase(f):
    maiu = f.upper()
    mini = f.lower()
    caputa = f.title()

    print("{} \n{} \n{}".format(maiu, mini, caputa))

f = input("digite a frase: ")

frase(f)