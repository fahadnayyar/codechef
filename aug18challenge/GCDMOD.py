p = 10**9+7
t=  int(input())
for w in range(t):
	yoar = list(map(int,input().split()))
	a = yoar[0]
	b = yoar[1]
	n = yoar[2]
	if a==b:
		ans=(pow(a,n,p)+pow(b,n,p))%(p)
		print(ans)
		continue
	num = (pow(a,n,a-b) + pow(b,n,a-b))%(a-b)
	num1 = a-b

	x = num1
	y = num
	while(y>0):
		r = x%y
		x = y
		y = r
	print(x%p)	