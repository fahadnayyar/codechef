
from math import log
from math import exp
def root(n, k):

    yo=log(n)/k
    ro=exp(yo)
    r=int(ro)
    #R = int(exp(log(N) / K))
    if r ** k < n:
        r += 1
    return r
def array_de(n, k):
    if k == 1:
        return [n]
    r = root(n, k)
    while True:
        if n % r == 0:
            return [r] + array_de(n // r, k-1)
        r += 1






t=int(input())
for w in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	c=yoar[1]
	far=[]
	far=array_de(c,n)
	far.sort()
	#print(far)
	ans=far
	ll=len(ans)	
		#print(ans)
	bhagg=ll-1
	for i in range(ll-1,0,-1):
		if ans[i]-ans[i-1]<=1:
			bhagg=i-1
		else:
			break	
	yo=0
	#print(ans)
	for i in range(bhagg):
		print(ans[i]+yo,end=" ")
		yo+=1
	for i in range(ll-1,bhagg-1,-1):
		if i==bhagg:
			print(ans[i]+yo)
		print(ans[i]+yo,end=" ")
		yo+=1
	print()				          