from random import *
print(2)
for j in range(2):
	n=100000
	q=100000
	print(n,q)
	for i in range(n):
		print(randint(10**8,10**9),end=" ")
	print()
	for i in range(q):
		l= randint(1,n);
		r = randint(l,n)
		print(randint(1,2),l,r)	