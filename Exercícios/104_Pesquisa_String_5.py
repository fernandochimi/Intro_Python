string = "TTAAC"
contador = {}

for letra in string:
	if letra in contador:
		contador[letra]+=1
	else:
		contador[letra]=1

for chave in contador:
	print("%s %dx" % (chave, contador[chave]))