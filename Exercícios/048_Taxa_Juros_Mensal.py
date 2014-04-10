mes = 0
acumulado = 0
deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros de sua poupança: "))

while mes < 24:
	deposito_mensal = float(input("Digite o depósito mensal: "))
	acumulado = deposito_mensal + (acumulado + (taxa_juros * deposito_inicial))
	mes = mes + 1
	print("Mês %d: %5.2f." % (mes, acumulado))
print("O total acumulado de juros foi de R$ %5.2f." % acumulado)