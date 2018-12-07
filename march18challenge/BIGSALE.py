t=int(input())
for i in range(t):
	n=int(input())
	loss=0
	for j in range(n):
		arr=list(map(int,input().split()))
		p=arr[0]
		q=arr[1]
		d=arr[2]
		currloss=((p*(d**2))/10000)*q
		loss+=currloss
	print(loss)	