parenteses = input("Digite a sequência de parenteses: ")
x=0
pilha = []
while x < len(parenteses):
	if (parenteses[x] == "("):
		pilha.append("(")
	if (parenteses[x] == ")"):
		if(len(pilha) > 0):
			topo = pilha.pop(-1)
		else:
			pilha.append(")")
			break
	x = x+1
if(len(pilha)==0):
	print("OK")
else:
	print("Erro")