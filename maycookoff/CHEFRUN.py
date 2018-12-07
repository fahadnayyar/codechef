t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	x1=yoar[0]
	x2=yoar[1]
	x3=yoar[2]
	v1=yoar[3]
	v2=yoar[4]
	t1=(x3-x1)/v1
	t2=(x2-x3)/v2
	if (t1<t2):
		print("Chef")
	elif (t2<t1):
		print("Kefa")
	else:
		print("Draw")	