def gcd(a,b):
	if a==0:
		return b
	return gcd(b%a,a)
t = int(input())
for w in range(t):
	yoar = list(map(int,input().split()))
	n = yoar[0]
	a = yoar[1]
	k = yoar[2]
	# dd = ((720//n)-(2*a))//(a-1)
	# kth = a + (k-1)*d
	# print(kth)
	num = a*(n-1)*n + (k-1)*(360*(n-2)-2*a*n)
	dem = n*(n-1)
	#print(num,dem)
	gcc = gcd(num,dem)
	num=num//gcc
	dem=dem//gcc
	print(num,dem)