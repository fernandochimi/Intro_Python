L=[15,7,27,39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x=0
while x < len(L):
	if L[x]==p:
		print("%d achado na posição %d" % (p,x))
		break
	#x += 1
	if L[x]==v:
		print("%d achado na posição %d" % (v,x))
		break
	x += 1
else:
	print("%d e %d não encontrados" % p, v)