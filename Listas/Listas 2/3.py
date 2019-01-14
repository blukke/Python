# Turma B
# Exercício número 3 por Juan Lucas Melo de Borba

lista = [] # cria a lista compra vazia
print("Digite a lista de series desejadas para armazenamento, digite fim para sair") # mensagem
while True: # enquanto verdadeiro (loop infinito)
    titulo = input("Nome: ") # lê o titulo digitado
    if titulo.upper() == "FIM": # se for digitado fim
        break # encerra o loop infinito
    lista.append(titulo) # adiciona o titulo digitado na lista
print("="*90)
print("Lista de séries: ") # mensagem
for serie in lista: # para cada produto na lista compras
    print(serie) # imrpime o produto
print("="*90)