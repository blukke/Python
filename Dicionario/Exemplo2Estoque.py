estoque = {"Tomate": [1000, 2.30],
           "Alface": [500, 0.45],
           "Batata": [200, 1.20],
           "Feijão": [100, 1.50]}  # cria estoque
venda = [["Tomate", 5], ["Batata", 10], ["Alface", 5]]  # cria a lista de itens vendidos
total = 0
print("="*100)
print("Vendas: ")
for operacao in venda:  # para cada operação na lista venda
    produto, quantidade = operacao  # lê a lista de vendas setando o produto e quantidade de acordo com a posição apontada pela operação (0, 1, 2,)
    preco = estoque[produto][1]  #  busca no dicionário estoque o preço do produto indicado informando o produto obtido na lista vendas e a voluna 1 que representa o preço
    custo = preco * quantidade  # calcula o custo do produto indicado informando o produto obtido na lista vendas e a coluna 1 que representa o preço
    print("%10s: %d X %6.2f = %6.2f" % (produto, quantidade, preco, custo)) #  imprime as informações do produto atual do laço de repetição
    estoque[produto][0] -= quantidade  # acessa o produto na tabela estoque e altera seu campo 0 (quantidade) subtraindo a quantidade comprada
    total += custo  # acrescenta o custo obtido ao total
print("Custo total: %6.2f \n" % total)  # imprime o total
print("="*100)
print("Estoque: \n")
for chave, dados in estoque.items():  # para cada chave e dado nos itens do dicionário estoque
    print("Dscrição: ", chave)  # imprime chave
    print("Quantidade: ", dados[0])  # imprime o dado na posiçÃO 0
    print("Preço: %6.2f \n" % dados[1])  # imprime o dado na posição 1

