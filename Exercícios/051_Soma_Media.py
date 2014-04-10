s = 0
num = 0
while True:
	v = int(input("Digite um número para somar ou 0 para sair: "))
	if v == 0:
		break
	num = num + 1
	s = s+v
	m = s/num
print("Quantidade de números digitados: %d. \nSoma dos números: %d. \nMédia: %2.2f." % (num, s, m))