import math
# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-

#1

num = int(input('Digite um númerozinho: '))
ant = num - 1
suc = num + 1

print('O número digitado foi {}, o seu antecessor é {} e o seu sucessor é {}.'.format(num, ant, suc))

#2
nome = input('Digite seu nome: ')
nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))

###média é a soma dividido pela quantidade de elementos

med = (nota1 + nota2)/2
print('Caro {}, sendo a sua primeira nota {} e a sua segunda nota {}, a sua média é {}'.format(nome, nota1, nota2, med))


#3 conversor de um numero em metros e cm
num1 = float(input('Digite um número: '))
metros = num1/100
print('O número digitado equivale em cm {}cm e em metros {}m'.format(num1, metros))


#4 solicitar numero inteiro e retornar tabuada até o 10 do mesmo
numint = int(input('Digite um número inteiro; '))
tab1 = numint*1
tab2 = numint*2
tab3 = numint*3
tab4 = numint*4
tab5 = numint*5
tab6 = numint*6
tab7 = numint*7
tab8 = numint*8
tab9 = numint*9
tab10 = numint*10
print('A tabuada até o 10 de {} é \n {}x1 = {} \n {}x2 = {}\n {}x3 = {} \n {}x4 = {} \n {}x5 = {} \n {}x6 = {} \n {}x7 = {} \n {}x8 = {} \n {}x9 = {} \n {}x10 = {}'.format(numint, numint, tab1, numint, tab2,numint, tab3, numint, tab4, numint, tab5, numint, tab6, numint, tab7, numint, tab8, numint, tab9, numint, tab10))

#5
real = float(input('Digite o valor em real: '))
usd = real/4.11

print('O valor em dólares será de {:.2f}'.format(usd))


#6

print('Calculadora de quanto de tinta será necessário para pintar a sua parede')
w = float(input('Digite a largura da sua parede em metros: '))
h = float(input('Digite a altura da sua parede em metros: '))
a = w*h #w= largura e h= altura
t = a/2
print('A quantidad de tinta necessária para pintar a sua parede é de {} litros '.format(a/t))

#7

print('Olá, digite aqui o preço do produto desejado, que lhe informarei seu valor com os 5% de desconto')
v = float(input('Digite o valor: R$ '))
r = v - (v*5/100)

print('O valor do produto com o desconto será de R$ {}'.format(r))

#8

sal = float(input('Digite o seu salário atual:R$ '))
aum = sal + (sal*15/100)
print('O seu salário após o aumento será de: R$ {}'.format(aum))

#9 - que?

#10

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = co ** 2 + ca ** 2
raiz = math.sqrt(hip)
print('A hipotenusa será {:.2f}'.format(raiz))


#11

ang = float(input('angulo desejado: '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O seno do valor informado e de {:.2f}, o seu cosseno e de {:.2f} e sua tangente sera {:.2f}'.format(seno, cose, tang))



#12

print('IMC')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)
print('Com o seu peso de {}, e sua altura de {}, o seu IMC sera de {:.2f}.'.format(peso, altura, imc))



