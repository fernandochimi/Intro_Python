valor_casa = float(input("Digite o valor da casa a comprar: "))
salario = float(input("Digite seu salário: "))
anos_pagar = int(input("Digite a quantidade de anos que irá pagar a casa: "))

prestacao_casa = valor_casa / (anos_pagar*12)

if prestacao_casa > (salario * 0.30):
	print("Empréstimo rejeitado. Você pagaria R$ %5.2f. A prestação ultrapassa 30 porcento de seu salário!" % prestacao_casa)
else:
	print("Empréstimo aprovado! Você pagará R$ %5.2f durante %d anos." % (prestacao_casa, anos_pagar))