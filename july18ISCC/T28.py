def binSearch(arr,n,kya):
	l=0
	r=n-1
	while (l<=r):
		mid=(l+r)//2
		if arr[mid]==kya:
			return mid
		elif arr[mid]>kya:
			r=mid-1
		else:
			l=mid+1
	return -1			
	
def modInverse(a, m) :
	m0 = m
	y = 0
	x = 1
	if (m == 1) :
		return 0
	while (a > 1) :
 
    
		q = a // m
 
		t = m
 

		m = a % m
		a = t
		t = y
 
        
		y = x - q * y
		x = t
 
 

	if (x < 0) :
		x = x + m0
 
	return x				

yoar = list(map(int,input().split()))
n=yoar[0]
q=yoar[1]
a=[0]*n
b=[0]*n
c=[0]*n
#arr=[0]*n
arr=[]
for i in range(n):
	yoar = list(map(int,input().split()))
	a[i]=max(yoar[0],yoar[1])
	b[i]=min(yoar[0],yoar[1])
	xx=min(2*a[i],2*b[i]+1)
	yy=max(2*a[i],2*b[i]+1)

	if yy==xx+1:

		c=min(2*a[i],2*b[i]+1)
		arr.append(c)
dic = {}
for i in arr:
	dic[i]=0
for i in arr:
	dic[i]+=1
arr=list(set(arr))
arr.sort()
l=len(arr)

q = list(map(int,input().split()))
#print(dic)
for i in q:
	yo = binSearch(arr,l,i)
	if yo==-1:
		print(-1)
	else:
		elem = dic[i]
		print(modInverse(elem,1000000009))			



