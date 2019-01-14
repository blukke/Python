tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}  # Gera a tabela
print(tabela)  # imprime a tabela toda em linha reta
print("1 " + "=" * 100)  # Divisor
print(tabela["Tomate"])  # imprime só o preço do tomate
print("2 " + "=" * 100)  # Divisor
tabela["Tomate"] = 2.50  # Altera o preço  do tomate para 2.50 , pois ja existia a chave "Tomate"
print(tabela)
print("3 " + "=" * 100)
tabela["Cebola"] = 1.20  # adiciona Ceblo 1.20 na tabela, pois a chave "Cebola" não existia
print(tabela)
print("4 " + "=" * 100)
# print(tabela["Manga"]) #  -> Erro de KeyError, pois a chave de "Manga" não está na tabela
print("manga" in tabela) # imprime True se a chave Manga estiver na tabela ou False se não estiver
print("5 " + "=" * 100)  # divisor
print(tabela.keys())  #imrpime as chaves
print(tabela.values())  #imprime os valores
print("6 " + "=" * 100)  # divisor
del(tabela["Tomate"])
print(tabela)
print("7 " + "=" * 100)
tabela2 = {"Alface": [1000, 0.45],
          "Batata": [500, 1.20],
          "Tomate": [200, 2.30],
          "Feijão": [100, 0.45]}  # Gera a tabela utilizando lista nos valores
print(tabela2)