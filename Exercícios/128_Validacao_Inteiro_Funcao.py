# -*- coding: utf-8 -*-
def faixa_int(pergunta, minimo, maximo):
	while True:
		v=int(input(pergunta))
		if v<minimo or v>maximo:
			print("Valor inválido. Digite um valor entre %d e %d" % (minimo, maximo))
		else:
			return v