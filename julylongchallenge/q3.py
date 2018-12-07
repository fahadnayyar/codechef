t=int(input())
for w in range(t):
	s=input()
	n=len(s)
	arr=[]
	for i in s:
		arr.append(ord(i)-ord("a"))
	
	mainar=[]
	mainar1=[]
	for i in range(n):
		char=[]
		char1=[]
		for j in range(26):
			char.append(0)
			char1.append(0)
		mainar.append(char)
		mainar1.append(char1)
	
	for i in range(n-2,-1,-1):
		curar=mainar[i]
		nextar=mainar[i+1]
		curel=arr[i]
		nextel=arr[i+1]
		for j in range(26):
			if j>=nextel:
				curar[j]=nextar[j]+1
			else:
				curar[j]=nextar[j]	

	for i in range(1,n):
		curar=mainar1[i]
		prevar=mainar1[i-1]
		curel=arr[i]
		prevel=arr[i-1]
		for j in range(26):
			if j>=prevel:
				curar[j]=prevar[j]+1
			else:
				curar[j]=prevar[j]	

	summainar=mainar
	summainar1=mainar1


	ansar1=[]

	for i in range(n):

		curel=arr[i]
	
		sumaar=summainar[i]

		sumaaarl=summainar1[i]
		if curel<25:
			anss=sumaar[25]-sumaar[curel]
		else:
			anss=0	
		if curel>0:
			anssl=sumaaarl[curel-1] 
		else:
			anssl=0	

		ansar1.append(anss+anssl)

	acans=sum(ansar1)//2

 
 	
 
	gmax=0
	for i in range(n):
		curel=arr[i]

		sumarl=summainar1[i]

		sumarr=summainar[i]

		
		for j in range(26):
			curdif=j-curel
			if curdif>0:
				
				
				ghatar= sumarr[j]- sumarr[curel] #+ rar[curel+1]      # sum(rar[curel+1:j+1]) #decrement
				if curel==0:
					fayedal=sumarl[j-1]
				else:
					
					fayedal=sumarl[j-1]-sumarl[curel-1] #+ lar[curel]       # sum(lar[curel:j])  # increment
				curdifinc=(abs(curel-j)) # increment
				totaldec=ghatar - fayedal - curdifinc
				if gmax<totaldec:
					gmax=totaldec
			elif curdif<0:	
				fayedar= sumarr[curel] - sumarr[j] #+ rar[j+1]		# sum(rar[j+1:curel+1]) # increment
				if j==0:
					gatal=sumarl[curel-1]
				else:	
					gatal=sumarl[curel-1] - sumarl[j-1]	#+ lar[j]		#sum(lar[j:curel]) # decrement
				curdifinc=(abs(curel-j)) # increment
				totaldec=gatal- fayedar - curdifinc
				if gmax<totaldec:
					gmax=totaldec

	ans=(acans-gmax) 
	print(ans)				
 
 
 
	