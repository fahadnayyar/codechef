def bitsbata(num):
     binary = bin(num)[2:]
     return len(binary) 
# def ret2(bits):
# 	return 2**(bits-1)
# def ret3(bits):	

t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	k=yoar[1]
	bits=bitsbata(k)
	if n%2==0:
		if (k==1):
			print("1 "*n)
		else:
			
			yo=2**(bits-1)
			yo1=yo-1
			print(yo,end=" ")
			print(yo1,end=" ")
			if n>2:
				print("1 "*(n-2))
			else:
				print()	
	else:
		if (k==3 and n==3):
			print("3 3 3")
		elif (k==1):
			print("1 "*n)
		else:	
			if n==1:
				print(k)
			elif k==2:
				print("2 "*n)	
			else:	
				yo=2**(bits-1)
				yo1=2**(bits-2)
				yo3=yo1-1
				print(yo,end=" ")
				print(yo1,end=" ")
				print(yo3,end=" ")
				if n>3:
					print("1 "*(n-3))
				else:
					print()	