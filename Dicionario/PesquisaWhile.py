L = [5, 10, 15, 20, 25]  # cria uma lista
p = int(input("Digite o valor procurado: "))  # entrada de dados
achou = False # Defina a variável achour para Falso
x = 0  # Define x como 0
while x < len(L):  # Enquanto x for menor que o  comprimento da Lista
    if L[x] == p:  # Se o numero na posição x for igual ao valor procurado
        achou = True  # achou recebe verdadeiro
        break  # Quebra o laço
    x += 1  # x recebe o valor atual mais 1
if achou:  # se achou
    print("{} encontrado na posição {}".format(p, x))  # Saida de dados
else:  # se não achou
    print("{} não encontrado".format(p))  # saida de dados


