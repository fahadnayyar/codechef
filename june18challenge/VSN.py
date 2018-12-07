def det(a):
	#print(a[2][2])
	yo1=a[0][0]*((a[1][1]*a[2][2])-(a[1][2]*a[2][1]))
	yo2=a[0][1]*((a[1][0]*a[2][2])-(a[1][2]*a[2][0]))
	yo3=a[0][2]*((a[1][0]*a[2][1])-(a[2][0]*a[1][1]))
	return yo1-yo2+yo3
	#return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[2][0]*a[1][1])
from math import *
t=int(input())
for i in range(t):
	yoar=list(map(int,input().split()))
	px=yoar[0]
	py=yoar[1]
	pz=yoar[2]
	qx=yoar[3]
	qy=yoar[4]
	qz=yoar[5]
	dx=yoar[6]
	dy=yoar[7]
	dz=yoar[8]
	cx=yoar[9]
	cy=yoar[10]
	cz=yoar[11]
	r=yoar[12]
	a=-dy*(pz-cz)+dz*(py-cy)
	b=-dz*(px-cx)+dx*(pz-cz)
	c=-dx*(py-cy)+dy*(px-cx)
	#print(a,b,c)
	#a=[[a,b,c],[px,py,pz],[cx,cy,cz]]
	#print(aa[0][0])
	M1=det([[a,b,c],[px,py,pz],[cx,cy,cz]])
	#print(M1)
	Ml1=det([[0,b,c],[1,py,pz],[r+1,cy,cz]])
	#print(Ml1)
	Mm1=det([[a,0,c],[px,1,pz],[cx,r+1,cz]])
	#print(Mm1)
	Mn1=det([[a,b,0],[px,py,1],[cx,cy,r+1]])
	#print(Mn1)
	M2=det([[a,b,c],[px,py,pz],[cx,cy,cz]])
	#print(M2)
	Ml2=det([[0,b,c],[1,py,pz],[-r+1,cy,cz]])
	#print(Ml2)
	Mm2=det([[a,0,c],[px,1,pz],[cx,-r+1,cz]])
	#print(Mm1)
	Mn2=det([[a,b,0],[px,py,1],[cx,cy,-r+1]])
	#print(Mn2)
	l1=Ml1/M1
	m1=Mm1/M1
	n1=Mn1/M1
	l2=Ml2/M2
	m2=Mm2/M2
	n2=Mn2/M2
	#print(l1*a+m1*b+n1*c)
	#print(l1,m1,n1,l2,m2,n2)
	#print(l1**2+m1**2+n1**2)
	t1=-1
	t2=-1
	if (l1*dx+m1*dy+n1*dz) !=0:
		t1=(1-(l1*qx+m1*qy+n1*qz))/(l1*dx+m1*dy+n1*dz)
	if 	(l2*dx+m2*dy+n2*dz)!=0:
		t2=(1-(l2*qx+m2*qy+n2*qz))/(l2*dx+m2*dy+n2*dz)
	#print(t1,t2)
	if t2<0 and t2<0:
		print(-1)
	elif t1<0:
		print(t2)
	elif t2<0:
		print(t1)
	else:
		print(min(t2,t1))			
	# x1=px-cx
	# y1=py-cy
	# A=(x1**2-r**2)
	# if A==0:
	# 	m1=(r**2-y1**2)/(2*x1*y1)
	# 	#m1=(r**2-y1**2)/(2*m*x1*y1)
	# 	t1=(py+m1*px+qy-m1*qx)/(m1*dx-dy)
	# 	print(t1)
	# else:
	# 	m1=(x1*y1+r*(sqrt((x1**2)+(y1**2)-(r**2))))/(A)
	# 	m2=(x1*y1-r*(sqrt((x1**2)+(y1**2)-(r**2))))/(A)
	# 	t1=(-py+m1*px+qy-m1*qx)/(m1*dx-dy)
	# 	t2=(-py+m2*px+qy-m2*qx)/(m2*dx-dy)
	# 	if t1<0 and t2<0:
	# 		print(-1)
	# 	elif t1<0:
	# 		print(t2)
	# 	elif t2<0:
	# 		print(t1)
		
	# 	else:
	# 		print(min(t1,t2))		
	# 	# print(max(t1,t2))
	# 	# print(t1,t2)