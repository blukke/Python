mensagem = 'tecnico em informatica'
print(len(mensagem)) #mosttra tamanho do vetor
print(mensagem.count('t')) #verifica quantas letras dentro as aspas contem na string
print(mensagem.count('o', 0, 7)) #verifica quantas letras 'o' existem na frase da posicao 0 ate 6 (7-1)
print(mensagem.find('om')) #retorna o indice em que a palavra 'em' se inicia, caso a encontre, caso contrario exibe o valor -
print('em' in mensagem)
