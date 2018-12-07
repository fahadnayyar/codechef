def isrect(a):
	if a[0]==a[1] and a[2]==a[3] or a[0]==a[2] and a[1]==a[3] or a[0]==a[3] and a[1]==a[2]:
		return True
	else:
		return False	
#print(isrect([2,1,3,2]))

n=int(input())
for i in range(n):
	par=list(map(int,input().split()))
	if isrect(par):
		print("YES")
	else:
		print("NO")	


