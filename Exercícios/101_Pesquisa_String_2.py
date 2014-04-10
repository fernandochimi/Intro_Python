string1="AABBEFAATT"
string2="BE"
p=0
p=string1.find(string2, p)
if p>=0:
	print("%s encontrado na posição %d" % (string2, p))