t=int(input())
for i in range(t):
	s=input()
	l=len(s)
	if l<4:
		print("normal")
	else:
		count=0
		for j in range(3,l):
			flag1=0
			flag2=0
			flag3=0
			flag4=0


			subs=s[j-3:j+1]
			
			#asci=sum(map(ord, subs))
			
			#if asci==406:
			#	count+=1
			#if subs=="" or subs=""
			for k in subs:
				if k=="c":
					flag1=1
				elif k=="h":
					flag2=1
				elif k=="e":
					flag3=1
				elif k=="f":
					flag4=1
			if flag1==1 and flag2==1 and flag3==1 and flag4==1:
				count+=1		
		if count==0:
			print("normal")			
		else:
			print("lovely "+str(count))	
