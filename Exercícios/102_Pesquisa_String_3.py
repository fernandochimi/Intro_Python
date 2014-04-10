string1 = "AAACTBF"
string2 = "CBT"
string3 = ""
for letra in string1:
	if letra in string2 and letra not in string3:
		string3+=letra
print("%s" % string3)