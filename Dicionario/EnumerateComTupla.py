L = [4, 10, 8, 20, 12]
for z in enumerate(L):  # enumerate pega o índice e o número na posição
    x, e = z  # z neste caso é uma tupla
    print("[%d] %d" % (x, e))  # imprime indice e o valor
    print(z)

