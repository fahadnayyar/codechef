t=int(input())
for w in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	k=yoar[1]
	s=input()
	presumar=[]
	presumar.append(0)
	for i in range(1,n):
		if (s[i]!=s[i-1]):
			presumar.append(presumar[i-1]+1)
		else:
			presumar.append(presumar[i-1]+0)
	ans=0
	for i in range(1,n-k+1):
		ans+=presumar[i+k-1]-presumar[i-1]
	print(ans)				