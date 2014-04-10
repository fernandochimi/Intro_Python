minutos = int(input("Digite os minutos utilizados: "))

if minutos < 200:
	preco = 0.20
else:
	if minutos < 400:
		preco = 0.18
	else:
		preco = 0.15

print("Você vai pagar este mês R$ %5.2f." % (minutos * preco))