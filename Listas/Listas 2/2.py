# Turma B
# Exercício número 2 por Juan Lucas Melo de Borba

#def cresc(a):  # tentei fazer com função e falhei miseravelmente, mas elas deu certo.
    #sorted(a)

#def dec(a):
   #sorted(a, reverse=True)

numeros = (8, 9, 5, 7, 48, 13, 17, 666, 14, 20)  # tupla
digitado = input("Digite 'cresc' para crescente e 'dec' para decrescente: ")

if digitado == "cresc":
    #cresc(numeros   )
    print("Os numeros em ordem crescente são", sorted(numeros))
elif digitado == "dec":
   #dec(numeros)
    print("Os numeros em ordem decrescente são", sorted(numeros, reverse = True))