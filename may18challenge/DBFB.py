def fibo01(n):
	if n==1:
		return 0
	elif n==2:
		return 1	
	a=0
	b=1
	for i in range(n-2):
		c=a+b
		a=b
		b=c
	return b


def fibo10(n):
	if n==1:
		return 1
	elif n==2:
		return 0	
	a=1
	b=0
	for i in range(n-2):
		c=a+b
		a=b
		b=c
	return b

t=int(input())
for i in range(t):
	yo=list(map(int,input().split()))
	m=yo[0]
	n=yo[1]
	y01=fibo01(n)
	y10=fibo10(n)
	Ar=list(map(int,input().split()))
	Br=list(map(int,input().split()))
	suma=sum(Ar)
	sumb=sum(Br)
	ans=(m*suma*(y10))+(m*sumb*(y01))
	print(ans)