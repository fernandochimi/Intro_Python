# -*-coding: utf-8 -*-
x = 0
y = 0

def valor1(x):
	return(x)
def valor2(y):
	return(y)
def multiplo(x,y):
	if (valor1(x) % valor2(y) == 0):
		return ("%d é multiplo de %d" % (x, y))
	else:
		return ("%d não é multiplo de %d" % (x, y))

x = int(input("Num1: "))
y = int(input("Num2: "))
print (multiplo(x,y))