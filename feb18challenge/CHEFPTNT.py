t=int(input())
for i in range(t):
	yo=list(map(int,input().split()))
	n=yo[0]
	m=yo[1]
	x=yo[2]
	k=yo[3]
	s=input()
	if m%2==0:
		evmon=odmon=m//2
	else:
		odmon=m//2+1
		evmon=m//2	
	evwor=0
	odwork=0
	for i in s:
		if i=="E":
			evwor+=1
		else:
			odwork+=1
	evgrp=evwor//x
	evleft=evwor-(evgrp*x)
	odgrp=odwork//x
	odleft=odwork-(odgrp*x)
	if evgrp>=evmon:
		evgrp=evmon
		evleft=0
	if odgrp>=odmon:
		odgrp=odmon
		odleft=0
	total=(evgrp*x)+(odgrp*x)+evleft+odleft
	if total>=n:
		print("yes")		
	else:
		print("no")	
	