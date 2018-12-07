t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	m=yoar[1]
	arr=list(map(int,input().split()))
	count=0
	for i in arr:
		if i%m==0:
			count+=1
	print((2**count)-1)		
	# sumar=[]
	# sumar.append(arr[0])

	# for i in range(1,n):
	# 	sumar.append(arr[i]+sumar[i-1])
	# count=0
	# for i in range(n):
	# 	for j in range(i,n):
	# 		suma=sumar[j]-sumar[i]+arr[i]
	# 		if suma%m==0:
	# 			count+=1
	# print(count)				