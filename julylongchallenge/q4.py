def nCrModp(n, r):
 

	C = [0 for i in range(r+1)]
 
	C[0] = 1 
 

	for i in range(1, n+1):
 

		for j in range(min(i, r), 0, -1):
 

			C[j] = (C[j] + C[j-1]) 
 
	return C[r]
#from math import fac
def kaamkar(a,b,nn):
	ret=1
	for i in range(b):
		ret=((ret%nn)*(a%nn))%n
	return ret%nn	
nn=1000000007
t=int(input())

for w in range(t):
	yoar=list(map(int,input().split()))
	n = yoar[0]
	k = yoar[1]
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	ans=1
	
	for i in range(2,n-k+3):
		kav=k-2
		nav=n-i
		for j in range(i,n):
			#print(i,j)
			a=arr[j]
			#print(nav,kav)
			#print(nCrModp(nav , kav ))
			#print(nCrModp(nav-1,kav))
			b= nCrModp(nav , kav) - nCrModp(nav-1,kav)
			# if kav==1:
			# 	b=1
			# else:	
				
			print(a,b)
			ret =  kaamkar(a,b,nn)
			ans=((ans%nn)*ret)%nn
	print(ans)		
	











