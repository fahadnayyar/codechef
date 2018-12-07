#from copy import *
def gcd(a,b):
	if a==0:
		return b
	return gcd(b%a,a)	

t=int(input())

for i in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	
	yo=arr[0]
	for i in range(1,n):
		yo=gcd(yo,arr[i])
			
			
	if yo==1:
		print(0)
	else:
		print(-1)			







