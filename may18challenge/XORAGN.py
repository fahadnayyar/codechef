t=int(input())
for i in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	for j in range(n):
		arr[j]=arr[j]*2
	ans=0
	for j in range(n):
		ans=ans^arr[j]
	print(ans)		