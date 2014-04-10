mes = 0
acumulado = 0
divida_inicial = float(input("Digite o valor inicial da dívida: "))
taxa_juros = float(input("Digite a taxa de juros da dívida: "))
deposito_mensal = float(input("Digite o depósito mensal para cobrir a dívida: "))

while divida_inicial > deposito_mensal:
	deposito_mensal = float(input("Digite o depósito mensal para cobrir a dívida: "))
	acumulado = deposito_mensal - (taxa_juros * divida_inicial)
	mes = mes + 1
	print("Mês %d: %5.2f." % (mes, acumulado))
print("O total pago foi de R$ %5.2f." % acumulado)