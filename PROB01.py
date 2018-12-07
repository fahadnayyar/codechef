from math import sqrt
def is_prime(n):
	if n==1:
		return False
	if n==2:
		return True
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			return False
	return True		
# n=int(input())
# print(is_prime(n))	
t=int(input())
for i in range(t):
	n=int(input())
	if is_prime(n):
		print("yes")
	else:
		print("no")	