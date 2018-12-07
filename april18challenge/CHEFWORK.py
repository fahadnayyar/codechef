n=int(input())
c=list(map(int,input().split()))
t=list(map(int,input().split()))
ar1=[]
ar2=[]
ar3=[]
for i in range(n):
	if t[i]==1:
		ar1.append(c[i])
	elif t[i]==2:
		ar2.append(c[i])
	else:
		ar3.append(c[i])
if len(ar1)==0:
	yo1=0

else:
	yo1=min(ar1)				
if len(ar2)==0:
	yo2=0
else:

	yo2=min(ar2)
if len(ar3)==0:
	yo3=0
else:

	yo3=min(ar3)
if (yo3==0):
	print(yo1+yo2)
elif (yo1==0):
	print(yo3)
elif (yo2==0):
	print(yo3)	
elif (yo1+yo2<yo3):
	print(yo1+yo2)
else:
	print(yo3)	