L=[7,8,9,10]
p = int(input("Digite um número a pesquisar: "))
for e in L:
	if e == p:
		print("Elemento encontrado")
		break
else:
	print("Elemento não encontrado")