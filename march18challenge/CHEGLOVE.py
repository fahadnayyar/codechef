t=int(input())
for i in range(t):
	n=int(input())
	f=list(map(int,input().split()))
	g=list(map(int,input().split()))
	flag1=0
	flag2=0
	for i in range(n):
		if f[i]>g[i]:
			flag1=1
			break
	for i in range(n):
		if f[i]>g[n-(i+1)]:
			flag2=1
			break
	if flag1==0 and flag2==0:
		ans="both"
	elif flag1==0 and flag2==1:
		ans="front"	
	elif flag1==1 and flag2==0:
		ans="back"
	else:
		ans="none"
	print(ans)							