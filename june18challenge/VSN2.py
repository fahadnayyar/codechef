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
	qx=qx-px
	qy=qy-py
	qz=qz-pz
	lx=px-cx
	ly=py-cy
	lz=pz-cz
	A=(((-dx*ly+dy*lx)**2)+((dz*ly-dy*lz)**2)+((dx*lz-dz*lx)**2))-(r**2)*((dx**2)+(dy**2)+(dz**2))
	B=2*((((-qx*ly+qy*lx)*(-dx*ly+dy*lx))+((-qy*lz+qz*ly)*(dz*ly-dy*lz))+((-qz*lx+qx*lz)*(dx*lz-dz*lx)))-(r**2)*((dx*qx)+(dy*qy)+(dz*qz)))
	C=(((-qx*ly+qy*lx)**2)+((-qy*lz+qz*ly)**2)+((-qz*lx+qx*lz)**2))-(r**2)*((qx**2)+(qy**2)+(qz**2))
	if A==0 and B==0:
		print(-1)
	elif A==0:
		print(-C/B)
	elif B==0:
		print(sqrt(-C/A))
	else:
		t1=(-B+sqrt((B**2)-4*A*C))/(2*A)
		t2=(-B-sqrt((B**2)-4*A*C))/(2*A)		
		if t1<0 and t2<0:
			print(-1)
		elif t1<0:
			print(t2)
		elif t2<0:
			print(t1)
		else:
			print(min(t1,t2))		