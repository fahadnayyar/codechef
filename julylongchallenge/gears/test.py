from random import *
n=100000
m=200000
print(n,m)
for i in range(n):
	print(randint(6,1000000),end=" ")
for i in range(m):
	yo = randint(1,3)
	if yo==1:
		print(1,randint(1,n),randint(1,1000000))
	elif yo==2:
		print(2,randint(1,n),randint(1,n))
	else:
		v=randint(1,1000000)
		print(3,randint(1,n),randint(1,n),v)			
