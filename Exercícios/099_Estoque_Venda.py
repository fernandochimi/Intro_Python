estoque = {"Tomate": [1000, 2.30], "Alface": [500, 0.45], "Batata": [2001, 1.20], "Feijão": [100, 1.50]}
venda = [["Tomate", 5], ["Batata", 10], ["Alface", 5]]
total = 0
print("Vendas: \n")
for operacao in venda:
	produto, quantidade = operacao
	preco = estoque[produto][1]
	custo = preco * quantidade
	print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade, preco, custo))
	estoque[produto][0] -= quantidade
	total += custo
print("Custo Total: %21.2f\n" % total)
print("Estoque: \n")
for chave, dados in estoque.items():
	print("Descrição : ", chave)
	print("Quantidade: ", dados[0])
	print("Preço     : %6.2f \n", dados[1])