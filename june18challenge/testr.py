from random import *
n=100000
print(n)
for i in range(n):
	s=''
	for i in range(10):
		s+=chr(randint(0,25)+ord('a'))
	print(s)
q=100000
print(q)
for i in range(q):
	r=randint(1,n)
	s=''
	for i in range(10):
		s+=chr(randint(0,25)+ord('a'))
	print(r,s)	