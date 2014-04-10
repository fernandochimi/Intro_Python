preco = float(input("Digite o preco da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = preco * (desconto / 100)
preco_pagar = preco - valor_desconto
print("O desconto e de R$ %5.2f. O valor a pagar e de R$ %5.2f" % (valor_desconto, preco_pagar))