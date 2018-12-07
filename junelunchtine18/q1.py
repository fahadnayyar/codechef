t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	l=yoar[0]
	r=yoar[1]
	count=0
	for i in range(l,r+1):
		yo=i%10
		if (yo==3 or yo==2 or yo==9):
			count+=1
	print(count)		