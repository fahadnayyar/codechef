from random import *
t = randint(1,10)
print(t)
for i in range(t):
	n = randint(2,10000)
	print(n)
	for i in range(n):
		print(randint(1,1000000000),end=" ")
	print()	