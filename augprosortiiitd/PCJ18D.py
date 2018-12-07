t = int(input())
for w in range(t):
	yoar  =list(map(int,input().split()))
	n = yoar[0]
	b = yoar[1]
	print((n*(b-1)+1)//b)