t=int(input())
for w in range(t):
	yoarr=list(map(int,input().split()))
	r=yoarr[0]
	l=yoarr[1]
	c=yoarr[2]
	vin=yoarr[3]
	print(1-(((r**2)*c)/(4*l)))	