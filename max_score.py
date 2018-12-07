t=int(input())
for k in range(t):
	n=int(input())
	arr=[]
	for i in range(n):
		a=list(map(int,input().split()))
		a.sort(reverse=True)
		arr.append(a)
	ans=[]
	#flag=0
	for i in range(n-1,-1,-1):
		if i==n-1:
			ans.append(arr[i][0])
			#ans+=arr[i][0]
			prev=arr[i][0]
		else:
			for j in range(n):
				
				if arr[i][j]<prev:
					ans.append(arr[i][j])
					#ans+=arr[i][j]
					prev=arr[i][j]	
					#print(prev)
					break
				#elif j==n-1 and arr[i][j]>prev:
					#flag=1	
					
	if len(ans)!=n:
		print(-1)
	else:
		print(sum(ans))						
	
