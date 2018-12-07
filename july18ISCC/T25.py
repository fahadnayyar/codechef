t=int(input())
for w in range(t):
	yoar = list(map(int,input().split()))
	n = yoar[0]
	k = yoar[1]
	arr = list(map(int,input().split()))
	suma=0
	count=0
	maxcount=0
	# l=0
	# r=0
	# L=0
	# R=0
	glsum=0
	for i in range(n):
		if suma + arr[i]<=k:
			suma += arr[i]
			count+=1
			#r=i

		elif suma!=0:
			suma = suma - arr[i - count] + arr[i]
			#r=i
			#l=i-count+1
		if count>maxcount:
			glsum=suma			
		maxcount = max(count,maxcount)
		
	print(maxcount,k-glsum)		