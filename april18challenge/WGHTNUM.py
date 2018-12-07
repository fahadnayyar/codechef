t=int(input())

for i in range(t):
	yo=list(map(int,input().split()))
	n=yo[0]
	w=yo[1]
	
	
	if w<-9 or w>8:
		ans=0
		print(ans)
		continue
	elif n<10**9:
		bhagg=10**(n-2)
		if w==0:
			ans=bhagg*9
		elif w<0:
			ans=bhagg*(10+w)	
		else:
			ans=bhagg*(9-w)	 
	#if ans<(10**9)+7:
#
#		print(ans)	
#	else:
		print(ans%(10**9+7))
	else:
		bhagg=1
		roro=(n-2)//(10**9) # kaand yaha hai!
		rem=(n-2)-roro*(10**9)		
		for j in range(roro):
			bhagg=(bhagg*(10**9))%((10**9)+7)	
		bhagg=(bhagg*(10**rem))%(10**9+7)
		if w==0:
			ans=bhagg*9
		elif w<0:
			ans=bhagg*(10+w)	
		else:
			ans=bhagg*(9-w)	 
		#if ans<(10**9)+7:
	#
	#		print(ans)	
	#	else:
		print(ans%(10**9+7))	
