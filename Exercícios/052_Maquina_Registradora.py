soma = 0
num_compras = 0
while True:
	cod_prod = int(input("Digite o código do produto ou 0 para sair: "))
	if cod_prod != 0:
		qtde_comprada = int(input("Digite a quantidade do produto comprada: "))
		if cod_prod == 1:
			preco = qtde_comprada * 0.50
		elif cod_prod == 2:
			preco = qtde_comprada * 1
		elif cod_prod == 3:
			preco = qtde_comprada * 4
		elif cod_prod == 5:
			preco = qtde_comprada * 7
		elif cod_prod == 9:
			preco = qtde_comprada * 8
		elif cod_prod != 1 and cod_prod != 2 and cod_prod != 3 and cod_prod != 5 and cod_prod != 9:
			print("Código Inválido!!! Os códigos válidos são 1, 2, 3, 5 e 9")
			preco = 0
	else:
		break
	num_compras = num_compras + 1
	soma = soma + preco
print("Quantidade de compras: %d. \nValor total dos produtos: R$ %5.2f." % (num_compras, soma))