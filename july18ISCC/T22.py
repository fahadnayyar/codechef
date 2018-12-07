t=int(input())
for w in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	flag=0
	for i in arr:
		if i==1:
			flag=1
			break
	if flag==0:
		print(-1)
	else:
		for i in arr:
			if (i!=1) and ((i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 )or	i==2 or i==3 or i==5 or i==7):
				print(i)
				break					