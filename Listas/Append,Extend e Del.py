L = [] # Cria uma lista vazia
print(L) # imprime a lista
print(len(L))  # imprime a quantidade de itens na lista
L.append("a")  #  adiciona "a" na lista
L.append("b")  #  adiciona "a" na lista
print(L)  #  imprime a lists
print(len(L)) # imprime a quantidade de itens na lista
L.append(["c", "d", "e"])  # adiciona uma lista na lista na lista
print(L)  # imprime a lista
print(len(L))  # imprime a quantidade de itens na lista
L.extend(["f", "g", "h"])  # adiciona os itens nda lista na outra
print(L) # imprime a lista
print(len(L))
del L[2] # deleta o item na posição 2 da lista
print(L) # imprime a lista
print(len(L))  # imprime a quantidade de itens na lista
