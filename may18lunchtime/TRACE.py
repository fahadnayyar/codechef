t=int(input())
for p in range(t):
	n=int(input())
	a=[]
	for i in range(n):
		yoar=list(map(int,input().split()))
		a.append(yoar)
	bhagg=[]
	for i in range((2*n)-1):
		bhagg.append(0)
	for i in range(n):
		for j in range(n):
			bhagg[i-j+(n-1)]+=a[i][j]
	#print(bhagg)
	print(max(bhagg))					