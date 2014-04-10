distancia = float(input("Digite a distância em KM a ser percorrida: "))
base = distancia
valor_pagar = 0

if base <= 200:
	valor_pagar = base * 0.50
else:
	valor_pagar = base * 0.45

print("Você percorreu %5.2f. Você irá pagar R$ %5.2f." % (base, valor_pagar))