def giveNext1(x):
	ro =0
	nhob = 0
	rop = 0
	nextt = 0
	if x>0:
		ro = x & -(x)
		nhob = x + ro
		rop = x ^ nhob
		rop = rop//ro
		rop >>= 2
		nextt = nhob | rop
	return nextt
t = int(input())
for w in range(t):
	n = int(input())
	st = bin(n)[2:]
	#print(st)
	count1 = 0
	l = len(st)
	for i in st:
		if i=="1":
			count1+=1
	if count1 == 2:
		print(0)
	elif count1<2:
		if n%2==0:
			print(1)
		else:
			flag=0
			for i in range(l-1,-1,-1):
				if st[i]=="0":

					st = st[:i]+"1"+st[i+1:]
					flag=1
			if flag==1:
				print(int(st,2)-n)
			else:		
				print((1<<l))
	else:
		count=0
		ind=0
		for i in range(l):
			if st[i]=="1":
				count+=1
			if count == 2:
				ind = i
				break
		stt = st[:ind+1]+"0"*(l-ind-1)
		#print(stt)
		#print(st)
		num = int(stt,2)
		ans1 = abs(n-num)
		ans2 = abs(n-giveNext1(num))
		print(min(ans2,ans1))
		#print(min(abs(n-num)),abs(n-giveNext1(num)))						

