def binSearch(arr,n,kya):
	l=0
	r=n-1
	while(l<=r):
		mid=(l+r)//2
		if (arr[mid]>=kya):
			r=mid-1
		else:
			l=mid+1
	return l 			
n=int(input())
m=int(input())
arr=[0]*n
for w in range(m):
	yoar=list(map(int,input().split()))
	l=yoar[0]
	r=yoar[1]
	for j in range(l-1,r):
		arr[j]+=1
arr.sort()
q=int(input())

for w in range(q):
	kya=int(input())
	yo = binSearch(arr,n,kya)
	print(n-yo)