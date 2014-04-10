T=[-10,-8,0,1,2,5,-2,-4]
temp_min=T[0]
temp_max=T[0]
soma = 0
for e in T:
	if e < temp_min:
		temp_min = e
	if e > temp_max:
		temp_max = e
	soma = soma + e
print("Temperatura mínima: %d C" % temp_min)
print("Temperatura máxima: %d C" % temp_max)
print("Temperatura média: %d C" % (soma/len(T)))