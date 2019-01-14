L = [5, 10, 15, 20, 25]  # cria uma lista
p = int(input("Digite o valor procurado: "))  # entrada de dados
for e in L: # Para cada elemento na lista
    if e == p:  # Se o elemento atual for igual p (valor pesquisado)
        print("{} faz parte da lista.".format(p))  # saida de dados
        break # quebra o laço do for
else: # Se o break não for executado
    print("{} não encontrado.".format(p))  # saida de dados

