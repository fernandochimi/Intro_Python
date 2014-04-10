# -*-coding: utf-8 -*-
base = 0
altura = 0

def valor_base(base):
	return(base)
def valor_altura(altura):
	return(altura)
def area(base, altura):
	area = (valor_base(base)*valor_altura(altura))/2
	return ("A area do Triângulo é de %d" % (area))

base = int(input("Digite a base do Triângulo: "))
altura = int(input("Digite a altura do Triângulo: "))
print (area(base,altura))