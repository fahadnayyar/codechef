t = int(input())
for w in range(t):
	yoar = list(map(int,input().split()))
	n = yoar[0]
	x = yoar[1]
	arr = list(map(int,input().split()))
	flag=0
	for i in arr:
		if i>=x:
			flag=1
			break
	if flag==1:
		print("YES")
	else:
		print("NO")			
