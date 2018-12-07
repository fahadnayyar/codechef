t=int(input())
for i in range(t):
	yo=list(map(int,input().split()))
	n=yo[0]
	k=yo[1]
	arr=list(map(int,input().split()))
	ar1=[]
	ar2=[]
	for j in range(n):
		if j%2==0:
			ar1.append(arr[j])
		else:
			ar2.append(arr[j])
	ar1.sort(reverse=True)
	ar2.sort()
	#print (ar1)
	#print (ar2)
	j=0
	l1=len(ar1)
	l2=len(ar2)
	while j<k and j<l1 and j<l2:
		if (ar1[j]>ar2[j]):
			temp=ar1[j]
			ar1[j]=ar2[j]
			ar2[j]=temp
			j+=1
		else:
			break	
	#print(ar1)
	#print(ar2)	
	if sum(ar1)<sum(ar2):
		print("YES")	
	else:
		print("NO")	