def modInverse(a, m) :
	m0 = m
	y = 0
	x = 1
	if (m == 1) :
		return 0
	while (a > 1) :
 
    
		q = a // m
 
		t = m
 
 
		m = a % m
		a = t
		t = y
 
        
		y = x - q * y
		x = t
 
 
 
	if (x < 0) :
		x = x + m0
 
	return x
 
 
t=int(input())
for w in range(t):
	yoar = list(map(int,input().split()))
	n=yoar[0]
	k=yoar[1]
	if k==1:
		print(n)
	else:	
		yo = pow(k,n+1,1000000007)
		ro = ((yo%1000000007) - (k%1000000007))%1000000007
		jo = modInverse((k-1)%1000000007,1000000007)
		ans = ((ro%1000000007)*(jo%1000000007))%1000000007
		print(ans) 


# t=int(input())
# for w in range(t):
# 	yoar = list(map(int,input().split()))
# 	n=yoar[0]
# 	k=yoar[1]
# 	ans=0
# 	for i in range(n):
# 		ans = (ans%1000000007 + pow(k,(i+1),1000000007))%1000000007
# 	print(ans)	
