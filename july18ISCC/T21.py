t = int(input())
for w in range(t):
	yoar = list(input().split())
	m=yoar[0]
	n=yoar[1]
	mkitna=0
	for i in m:
		val=int(i)
		mkitna=(mkitna%3+val%3)%3
	nkitna=0
	for i in n:
		val=int(i)
		nkitna=(nkitna%3+val%3)%3
	ans =( mkitna%3*nkitna%3)%3
	print(ans)		