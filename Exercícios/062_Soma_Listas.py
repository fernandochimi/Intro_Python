L=[0,1,2,3]
x=0
while x < 4:
	print(L[x])
	x+=1
Z=[4,5,6,7]
x=0
while x < 4:
	print(Z[x])
	x+=1
L.extend(Z)
print(L)