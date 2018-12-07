def xorlelo(x):
	ans=0
	for i in range(1,x+1):
		ans=ans^i
	return ans	
t=int(input())
for i in range(t):
	x=int(input())
	#print(xorlelo(x))
	y=x%4
	if y==0:
		print(x)
	elif y==1:
		print(1)
	elif y==2:
		print(x+1)
	elif y==3:
		print(0)			