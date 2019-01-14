# Turma B
# Exercício número 7 por Juan Lucas Melo de Borba


def add(a, b):
    print(a + b)


def subt(a, b):
    print(a - b)


def multi(a, b):
    print(a * b)


def divi(a, b):
    print(float(a / b))



print("\n Calculadora de números e somente números ok? \n \n \n")

a = int(input("Digite o primeiro dito cujo: "))
b = int(input("Digite o segundo dito cujo: "))

indag = input("Digite: \n 1 para somar; \n 2 para subtrair; \n 3 para multiplicar; \n 4 para dividir. \n  ")

if indag == "1":
    add(a, b)

elif indag == "2":
    subt(a, b)

elif indag == "3":
    multi(a, b)

elif indag == "4":
    divi(a, b)

else:
    print("Não consigo te entender porque voce digitou de uma forma burra, tente novamente.")


