salario = float(input("Digite seu salario: "))
aumento = float(input("Digite o percentual de aumento: "))
valor_reajuste = salario * (aumento / 100)
reajuste = salario + valor_reajuste
print("O aumento foi de R$ %5.2f. O seu novo salario e de R$ %5.2f" % (valor_reajuste, reajuste))