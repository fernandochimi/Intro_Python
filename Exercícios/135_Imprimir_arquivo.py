import sys

if(len(sys.argv) != 2):
	print("\nUso: 135_Imprimir_arquivo.py numeros.txt\n\n")
else:
	nome=sys.argv[1]
	arquivo=open(nome,"r")
	for linha in arquivo.readlines():
		print (linha[:-1])
	arquivo.close()