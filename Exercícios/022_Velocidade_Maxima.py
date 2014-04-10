velocidade_carro = float(input("Digite a velocidade atingida: "))
limite = 80
multa = 5

if velocidade_carro <= limite:
	print("Parabéns! Você está na velocidade permitida")
if velocidade_carro > limite:
	print("Você está %d km acima do normal. Multa de R$ %5.2f." % (velocidade_carro-limite, (velocidade_carro-limite)*multa))
