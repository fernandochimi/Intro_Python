# -*-coding: utf-8 -*-
lado = 0

def valor1(lado):
	return(lado)
def area(lado):
	lado = valor1(lado)*valor1(lado)
	return ("A area do quadrado é de %d" % (lado))

lado = int(input("Digite o lado do quadrado: "))
print (area(lado))