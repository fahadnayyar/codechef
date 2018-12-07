arr=list(map(int,input.split()))
n=arr[0]
q=arr[1]
narr=list(map(int,input.split()))
for i in range(q):
	arryo=list(map(int,input.split()))
	l=arryo[0]
	r=arryo[1]
	#find a no. in range X 0<X<2^31 such that xors sum is max.
