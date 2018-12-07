def give1(s,l):
	count=0
	for i in range(l):
		if s[i]=="1":
			count+=1
	return count		
t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	a=yoar[0]
	b=yoar[1]
	sa=bin(a)[2:]
	la=len(sa)
	sb=bin(b-1)[2:]
	lb=len(sb)
	a1=give1(sa,la)
	b1=give1(sb,lb)
	if a==b:
		print(0)
	elif b==0:
		print(-1)
	elif b==1:
		if a==0:
			print(1)
		else:
			print(-1)
	else:
		if a1<b1:
			print((b1-a1)+1)					
		elif a1>b1:
			print(2)
		else:
			print(1)		



