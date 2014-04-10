kwh = float(input("Digite a quantidade de kWh consumida: "))
instalacao = int(input("Digite o tipo de instalação: \n 1 - Residência \n 2 - Comércio \n 3 - Indústria \n"))
kwh_pagar = 0

if instalacao == 1:
	if kwh <= 500:
		kwh_pagar = kwh * 0.40
	else:
		kwh_pagar = kwh * 0.65
elif instalacao == 2:
	if kwh <= 1000:
		kwh_pagar = kwh * 0.55
	else:
		kwh_pagar = kwh * 0.60
elif instalacao == 3:
	if kwh <= 5000:
		kwh_pagar = kwh * 0.55
	else:
		kwh_pagar = kwh * 0.60
else:
	print("Opção inválida")
print("O tipo de instalação é %d. Você consumiu %5.2f kWh e pagará R$ %5.2f." % (instalacao, kwh, kwh_pagar))