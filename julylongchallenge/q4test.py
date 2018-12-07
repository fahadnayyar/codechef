from random import *
t=10
print(t)
for i in range(t):
	n=5000
	print(n,randint(3,n))
	for j in range(n):
		print(j+1000,end=" ")
	print()	
