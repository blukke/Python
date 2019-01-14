def epar(x):  # Definição da função e seu parametro
    return x % 2 == 0  # Valor de retorno


def parOuImpar(y):  # Definição da função e seu parametro
    if epar(y):  # Chamada da função passando parametro
        return "par."  # Valor de retorno
    else:
        return "impar."  # Valor de retorno


#  Programa principal 2.0
num = int(input("Digite um número: "))  # Entrada de dados
print("%d é %s" % (num, parOuImpar(num)))  # Chamada da função