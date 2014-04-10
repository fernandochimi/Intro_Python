L=[]
while True:
	n = int(input("Digite um número (0 para sair): "))
	if n == 0:
		break
	n += 1
x = 0
for x in L:
	if x==n:
		print(L[x])
x = x+1