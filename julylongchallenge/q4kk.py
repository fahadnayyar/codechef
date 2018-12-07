def binomialcoefficient(n):
	x=[]
	for i in range(n+1):
		y=[]
		for i in range(n+1):
			y.append(0)
		x.append(y)
	for i in range(n+1):
		for j in range(i+1):
			if(i==j):
				x[i][j]=1
			elif(j==0):
				x[i][j]=1
			else:
				x[i][j]=(x[i-1][j]+x[i-1][j-1])%(1000000006)
	return x
def func(n,k,a,coefficients):
	#coefficients=binomialcoefficient(n)
	value=coefficients[n-1][k-1]
	ans=[value]*(n)
	#print(ans)
	for i in range(n-k+1):
		ans[i]-=coefficients[n-i-1][k-1]
		ans[i]=ans[i]%(1000000006)
	for i in range(k-1,n):
		ans[i]-=coefficients[i][k-1]
		ans[i]=ans[i]%(1000000006)	
	#print(ans)
	p=1
	mini=min(ans[1:-1])
	#print(mini,ans)
	for i in range(1,n-1):
		p=(p*(a[i]))%(1000000007)
	p=pow(p,mini,1000000007)
	for i in range(1,n-1):
		x=pow(a[i],ans[i]-mini,1000000007)
		p=p*x
		#print(p)
	return p%(1000000007)
 
def pow(x,y,p):
	res=1
	x=x%p
	while(y>0):
		if(y&1==1):
			res=(res*x)%p
		y=y//2
		x=(x*x)%p
	return res
ncrar=binomialcoefficient(5000)
t=int(input())
for i in range(t):
	a=[int(i) for i in input().split()]
	n=a[0]
	k=a[1]
	x=[int(i) for i in input().split()]
	x.sort()
	#ncrar=binomialcoefficient(5000)
	#print(binomialcoefficient(n))
	print(func(n,k,x,ncrar))