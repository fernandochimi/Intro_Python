a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
operacao = int(input("Digite a operação desejada: \n 1 - Soma (+) \n 2 - Subtração (-) \n 3 - Multiplicação (*) \n 4 - Divisão (/) \n"))

if operacao == 1:
	operacao = a + b
elif operacao == 2:
	operacao = a - b
elif operacao == 3:
	operacao = a * b
elif operacao == 4:
	operacao = a / b % 2
else:
	print("Operação inválida!")
print("O resultado é %5.2f." % operacao)