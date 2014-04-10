string1 = "AATTCGAA"
string2 = "TG"
string3 = "AC"
string4 = ""

if len(string2) == len(string3):
	string4 = ""
	for letra in string1:
		posicao = string2.find(letra)
		if posicao != -1:
			string4+=string3[posicao]
		else:
			string4+=letra

	print(string4) 