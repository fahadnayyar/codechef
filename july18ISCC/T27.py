def binSearch(arr,n,kya):
	l=0
	r=n-1
	while (l<=r):
		mid=(l+r)//2
		if arr[mid]==kya:
			return mid
		elif arr[mid]>kya:
			r=mid-1
		else:
			l=mid+1
	return -1	
from math import sqrt
t=int(input())
for w in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	sqrtar=[]
	for i in arr:
		yo = int(sqrt(i))
		if yo*yo==i:
			sqrtar.append(i*i)
	arr.sort()
	count=0
	#print(sqrtar)
	for r in sqrtar:
		for g in range(n):
			for f in range(g+1,n):
				gg = arr[g]**2
				ff = arr[f]**2

				c=gg+ff-r	
				print(c,gg,ff,r)
				yo = binSearch(arr,n,c)
				if (yo!=-1 ):
					print("yo")
					print(c,gg,ff,r)
					count+=1
	print(count)				