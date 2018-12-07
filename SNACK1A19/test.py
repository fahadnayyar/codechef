from random import *
print(1000)
for i in range(1000):
	a = randint(1,10**5-1)
	c = randint(a+1,10**5)
	b = c-a
	print(a,b,c)