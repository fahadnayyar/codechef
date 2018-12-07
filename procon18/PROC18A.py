#from math inport inf
t = int(input())
for w in range(t):
	yoar = list(map(int,input().split()))
	n = yoar[0]
	k = yoar[1]
	arr = list(map(int,input().split()))
	presum = [0]*(n)
	presum[0] = arr[0]
	for i in range(1,n):
		presum[i] = presum[i-1] + arr[i]
	maxa = 0
	for i in range(n-k+1):
		curr = presum[i+k-1] - presum[i] + arr[i]
		if curr>maxa:
			maxa = curr
	print(maxa)