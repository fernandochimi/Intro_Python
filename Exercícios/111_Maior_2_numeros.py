x = 0
y = 0

def valor1(x):
	return(x)
def valor2(y):
	return(y)
def maximo(x,y):
	if valor1(x) >= valor2(y):
		return ("%d maior que %d" % (x, y))
	elif valor1(x) <= valor2(y):
		return ("%d maior que %d" % (x, y))
	else:
		return ("%d igual a %d" % (x, y))

x = int(input("Num1: "))
y = int(input("Num2: "))
print (maximo(x,y))