quantidade_cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumados = int(input("Digite a quantidade de anos fumados: "))
anos_dias = anos_fumados * 365
tempo_cigarro = 10
minutos_horas = (tempo_cigarro/60)*quantidade_cigarros
horas_dias = minutos_horas /24

dias_vida_fumante = horas_dias * anos_dias
print("Voce perdeu %d dias de vida fumando." % dias_vida_fumante)