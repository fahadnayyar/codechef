t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	a=yoar[1]
	b=yoar[2]
	arr=list(map(int,input().split()))
	counta=0
	countb=0
	for i in arr:
		if i==a:
			counta+=1
		if i==b:
			countb+=1
	prob=(counta/n)*(countb/n)	
	print(prob)		