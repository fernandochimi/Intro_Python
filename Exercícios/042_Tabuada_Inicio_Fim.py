n = int(input("Tabuada de: "))
comeca_em = int(input("Começa em: "))
termina_em = int(input("Termina em: "))

while comeca_em <= termina_em:
	print("%d X %d = %d" % (n, comeca_em, (n*comeca_em)))
	comeca_em=comeca_em+1