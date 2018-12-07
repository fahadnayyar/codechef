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
	m=qy-py
	n=qx-px
	A=(cy*dx-cx*dy-py*dx+px*dy)**2-((r**2)*((dx**2)+(dy**2)))
	B=(2*(cy*dx-cx*dy-py*dx+px*dy)*(cy*n-cx*m-py*n+px*m))-(2*(r**2)*(n*dx+m*dy))
	C=((cy*n-cx*m-py*n+px*m)**2)-((r**2)*((m**2)+(n**2)))
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