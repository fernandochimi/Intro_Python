salario = float(input("Digite o salário: "))
base = salario
aumento = 0

if base > 1250:
	aumento = base + (base * 0.10)
if base <= 1250:
	aumento = base + (base * 0.15)

print("O salário foi reajustado para R$ %5.2f." % aumento)