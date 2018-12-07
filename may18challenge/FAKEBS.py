from copy import *
				
					
 
t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	q=yoar[1]
	arr=list(map(int,input().split()))
	dic={}
	for j in range(n):
		dic[arr[j]]=j	
 
	sorarr=deepcopy(arr)
	sorarr.sort()
	dic1={}
	for j in range(n):
		dic1[sorarr[j]]=j
 
	#print(dic)
	#print(dic1)
	for j in range(q):
		x=int(input())
		#ans=solve(arr,sorarr,x,n)
		if x not in dic:
			print(0)
			continue
 
		ind=dic[x]
		ind1=dic1[x]
		leftcont=ind1
		rightcount=n-ind1-1
		low=0
		high=n-1
		#count=0
		countbig=0
		countsmall=0
		#flag=0
		ans=0
		while (low<=high):
			mid=(low+high)//2
		
			if mid==ind:
				break
			elif mid<ind:
				if arr[mid]>x:
					countsmall+=1
				else:
					leftcont=leftcont-1	
				low=mid+1	
			elif mid>ind:
				if arr[mid]<x:
					countbig+=1
				else:
					rightcount=rightcount-1			
				high=mid-1
		if countbig>rightcount:
			ans=-1
		elif countsmall>leftcont:
			ans=-1
	
		else:		
			ans=max(countbig,countsmall)
 
 
 
		print(ans) 