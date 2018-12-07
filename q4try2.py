def giveNcr(n,p1):
	ret = [[0 for x in range(n+1)] for x in range(n+1)]
	for i in range(n+1):
		for j in range(i+1):
			if (j==0 or j==i):
				ret[i][j]=1
			else:
				ret[i][j]=(ret[i-1][j-1]%p1+ret[i-1][j]%p1)%p1
	return ret			

p=1000000007
p1=1000000006
t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	k=yoar[1]
	arr=list(map(int,input().split()))
	ncarar = giveNcr(n,p1)
	#print(ncarar)
	expoar = [ncarar[n-1][k-1] for x in range(n)]
	for i in range(n-k+1):
		expoar[i] = (expoar[i] - ncarar[n-i-1][k-1])%p1
	for i in range(k-1,n):
		expoar[i] = (expoar[i] - ncarar[i][k-1])%p1
	ans = 1
	for i in range(n):
		yo = pow(arr[i],expoar[i],p)
		ans = ((ans%p) * (yo%p))%p	
	print(ans)		
