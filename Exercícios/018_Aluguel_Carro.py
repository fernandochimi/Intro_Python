km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias que o carro ficou alugado: "))
valor_dias = 60
valor_km = 0.15
valor_a_pagar = (km_percorridos*valor_km)+(dias_alugados*valor_dias)
print("Voce percorreu %5.2f km em %d dias. Voce vai pagar R$ %5.2f." % (km_percorridos, dias_alugados, valor_a_pagar))