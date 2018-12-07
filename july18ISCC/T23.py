def gcd(a, b): 
    if a == 0 :
        return b 
     
    return gcd(b%a, a)
t=int(input())
for w in range(t):
	n=int(input())
	arr=list(map(int,input().split()))
	flag=0
	for i in range(n):
		for j in range(i+1,n):
			if gcd(arr[i],arr[j])==1:
				flag=1
				break
	if flag==0:
		print("NO")
	else:
		print("YES")	
