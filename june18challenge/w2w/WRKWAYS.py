from math import sqrt
#def give_ind():
def give_ind(x, arr,low, high):
	# if (low > high):
	# 	return -1
	# if (x <= arr[low]):
	# 	return low
	# elif x>arr[high]:
	# 	return -1	
	mid = int((low + high) / 2)
	if (arr[mid] == x):
		return mid
	# elif arr[mid]<x:
	# 	if mid+1<=high and x<=arr[mid+1]:
	# 		return mid+1
	# 	else:
	# 		return give_ind(x,arr,mid+1,high)
	# else:
	# 	if mid-1 >=low and x>arr[mid-1]:
	# 		return mid
	# 	else:
	# 		return give_ind(x,arr,low,mid-1)					
	if x>=arr[high]:
		return high


	if (mid > 0 and arr[mid-1] <= x and x < arr[mid]):
		return mid - 1
	if (x < arr[mid]):
		return give_ind(x,arr, low, mid-1)
	return give_ind(x,arr, mid+1, high)
def ret(c):
	ar=[]
	while (c%2==0):
		ar.append(2)
		c=c//2;
	for i in range(3,int(sqrt(c))+1,2):
		while c%i==0:
			ar.append(i)
			c=c//i
	if c>2:
		ar.append(c)
	return ar				
t=int(input())
for w in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	c=yoar[1]
	far=ret(c)
	#print(far)
	l=len(far)
	if l<=n:
		diff=n-l
		ans=[]
		for i in range(diff):
			ans.append(1)
		for i in far:
			ans.append(i)
		ll=len(ans)	
		#print(ans)
		bhagg=ll-1
		for i in range(ll-1,0,-1):
			if ans[i]-ans[i-1]<=1:
				bhagg=i-1
			else:
				break	
		yo=0
		#print(ans)
		for i in range(bhagg):
			print(ans[i]+yo,end=" ")
			yo+=1
		for i in range(ll-1,bhagg-1,-1):
			print(ans[i]+yo,end=" ")
			yo+=1
		print()				
	else:
		#l-i-1=n
		ind=l-n	
		diff=l-n
		for i in range(diff):
			yo=far[i]
			ro=far[ind]*yo
			xchind=give_ind(ro,far,ind,l-1)
			#print(far)
			#print(xchind)
			#print(far[xchind])
			#ro.remove(ind)
			#print(ind)
			far.insert(xchind+1,ro)
			ind+=1
			l+=1
		#print(far)
		ans=far[ind:]
		#print(ans)
		ll=len(ans)
		# temp=ans[0]
		# ans[0]=ans[ll-1]
		# ans[ll-1]=temp
		bhagg=ll-1
		for i in range(ll-1,0,-1):
			if ans[i]-ans[i-1]<=1:
				bhagg=i-1
			else:
				break	
		yo=0
		for i in range(bhagg):
			print(ans[i]+yo,end=" ")
			yo+=1
		for i in range(ll-1,bhagg-1,-1):
			print(ans[i]+yo,end=" ")
			yo+=1
		print()				

		# for i in range(ll):
		# 	print(ans[i]+i,end=" ")
		# print()








# from math import log
# from math import exp
# def root(n, k):

#     yo=log(n)/k
#     ro=exp(yo)
#     r=int(ro)
#     #R = int(exp(log(N) / K))
#     if r ** k < n:
#         r += 1
#     return r
# def array_de(n, k):
#     if k == 1:
#         return [n]
#     r = root(n, k)
#     while len():
#         if n % r == 0:
#             return [r] + array_de(n // r, k-1)
#         r += 1



# t=int(input())
# for w in range(t):
# 	yoar=list(map(int,input().split()))
# 	n=yoar[0]
# 	c=yoar[1]
# 	far=[]
# 	far=array_de(c,n)
# 	far.sort()
# 	ans=far
# 	ll=len(ans)	
# 		#print(ans)
# 	bhagg=ll-1
# 	for i in range(ll-1,0,-1):
# 		if ans[i]-ans[i-1]<=1:
# 			bhagg=i-1
# 		else:
# 			break	
# 	yo=0
# 	#print(ans)
# 	for i in range(bhagg):
# 		print(ans[i]+yo,end=" ")
# 		yo+=1
# 	for i in range(ll-1,bhagg-1,-1):
# 		print(ans[i]+yo,end=" ")
# 		yo+=1
# 	print()				          
