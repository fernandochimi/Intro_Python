ultimo = 0
fila1 = []
fila2 = []
while True:
	print("\nExistem %d clientes na fila 1 e %d clientes na fila 2." % (len(fila1), len(fila2)))
	print("Fila 1: ", fila1)
	print("Fila 2: ", fila2)
	print("Opções fila 1: F (Adiciona cliente), A (Realiza atendimento)")
	print("Opções fila 2: G (Adiciona cliente), B (Realiza atendimento)")
	print("S (Sair do programa)")
	operacao = input("Operação (F, A, G, B ou S): ")
	
	x = 0
	sair = False

	while x < len(operacao):
		if operacao[x] == "A" or operacao[x] == "F":
			fila = fila1
		else:
			fila = fila2
		if operacao[x] == "A" or operacao[x] == "B":
			if(len(fila)) > 0:
				atendido = fila.pop(0)
				print("Cliente %d atendido" % atendido)
			else:
				print("Fila vazia! Ninguém para atender.")
		elif operacao[x] == "F" or operacao[x] == "G":
			ultimo += 1 #incrementa ticket do novo cliente
			fila.append(ultimo)
		elif operacao[x] == "S":
			sair = True
			break
		else:
			print("Operação inválida! Digite apenas F, A ou S!" % (operacao[x], x))
		x = x + 1
	if(sair):
		break