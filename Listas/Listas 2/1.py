# Turma B

# Exercício número 1 por Juan Lucas Melo de Borba

vogais = ("A", "E", "I", "O", "U")  # variavel definindo vogais

n = 0

letras = ("A", "Y", "U", "P", "X", "J", "I", "L", "E", "W")  # tupla
print(letras)
print("="*100)

tam = len(letras)

for elemento in letras:
    if letras == vogais:
        n += 1

vog = vogais-1

print("A string possui {} letras, {} são vogais e {} são consoantes".format(tam, vog, con))



#if letras == vogais:
#    print("A string possui ")
#else:
#    print("É consoante")