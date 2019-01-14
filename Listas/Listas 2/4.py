# Turma B
# Exercício número 4 por Juan Lucas Melo de Borba

notas = []
med = 0

print("Digite as notas desejadas, digite fim para sair")
while True:  # enquanto verdadeiro (loop infinito)
    nota = input("Nota: ")
    if nota.upper() == "FIM": # se for digitado fim
        break # encerra o loop infinito
    notas.append(float(nota)) # adiciona o a nota digitada a lista de notas enquanto converte a mesma em float

for elemento in notas:
    med += elemento
tam = len(notas)
med = med / len(notas)

mai = notas[0]
men = notas[0]

for elemento in notas:
    if elemento < men:
        men = elemento
for elemento in notas:
    if elemento > mai:
        mai = elemento

print("="*90)
print("A menor nota é {}, a maior é {} e a sua média é de {:.2f}".format(men, mai, med))
