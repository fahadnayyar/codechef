from math import sqrt
from math import ceil
def binarysearch(arr,x):
	l=0
	r=len(arr)-1
	if(arr[l]>=x):
		return l
	elif(arr[r]<x):
		return -1
	while l<r:
		mid=l+(r-l)//2
		if(arr[mid]==x):
			return mid
		if(arr[mid]<x):
			if(mid+1<=r and x<=arr[mid+1]):
				return mid+1
			l=mid+1
		else:
			if(mid-1>=r and x>arr[mid-1]):
				return mid-1
			r=mid-1
	return l
def primefactors(n):
	arr=[]
	while(n%2==0):
		arr.append(2)
		n=n//2
	for i in range(3,ceil(sqrt(n))+1,2):
		while(n%i==0):
			arr.append(i)
			n=n//i
	if(n>2):
		arr.append(n)
	return arr
t=int(input())
for i in range(t):
	a=[int(j) for j in input().split()]
	n=a[0]
	c=a[1]
	if(n==1):
		print(c)
	else:
		ans=primefactors(c)
		if(n>len(ans)):
			a=n-len(ans)
			for i in range(a):
				ans.insert(0,1)
		elif(len(ans)>n):
			a=len(ans)-n
			j=a
			for i in range(a):
				x=ans.pop(0)
				y=ans.pop(j-1)
				xy=x*y
				l=binarysearch(ans,xy)
				if(l==-1):
					l=len(ans)+1
				ans.insert(l,xy)
				j=len(ans)-n
		ind=len(ans)-1
		for i in range(len(ans)-1,0,-1):
			if(ans[i]==ans[i-1]+1 or ans[i]==ans[i-1]):
				ind=i-1
			else:
				break
		for i in range(0,ind):
			print(i+ans[i],end=' ')
		ans=ans[ind:]
		ans.sort(reverse=True)
		for i in range(len(ans)):
			print(ans[i]+ind+i,end=' ')
		print()