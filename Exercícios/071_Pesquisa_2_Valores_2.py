L=[15,7,27,39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x=0
achoup = -1
achouv = -1
primeiro = 0
while x < len(L):
	if L[x]==p:
		achoup = x
	if L[x]==v:
		achouv = x
	x += 1
if achoup != -1:
	print("P: %d encontrado na posição %d" % (p, achoup))
else:
	print("%d não encontrado" % p)
if achouv != -1:
	print("V: %d encontrado na posição %d" % (v, achouv))
else:
	print("%d não encontrado" % v)

if achoup != -1 and achouv != -1:
	if achoup <= achouv:
		print("P achado antes de V")
	else:
		print("V achado antes de P")