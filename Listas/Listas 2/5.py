# Turma B
# Exercício número 5 por Juan Lucas Melo de Borba

print('IMC')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)

tabela = {"Peso: ": peso,
          "Altura: ": altura,
          "IMC: ": imc}

print(tabela)
#print('Com o seu peso de {}, e sua altura de {}, o seu IMC sera de {:.2f}.'.format(peso, altura, imc))