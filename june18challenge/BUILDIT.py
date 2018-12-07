# from __future__ import print_function
# import sys

# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)
def modInverse(a, m) :
	mm = m
	y = 0
	x = 1
	if (m == 1):
		return 0
 
	while (a > 1):
		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t
	if (x < 0) :
		x = x + mm
	return x
 
 
 
def giveind(i,x,h):
	if i+x-1<h:
		return i+x-1
	else:
		return i+x-1-(h-1)-1	
c=163577857		
n=int(input())
h=int(input())
x=int(input())
k=int(input())
ar=list(map(int,input().split()))
arr=[]
xarr=[]
for i in range(h):
	arr.append(0)
	xarr.append(0)
 
for i in ar:
	arr[i-1]+=1
#print(arr)
suma=0
for i in range(x):
	suma=(suma%c+arr[i]%c)%c
xarr[0]=suma

for i in range(1,h):
	#print(i,giveind(i,x,h))
	xarr[i]=((xarr[i-1]%c)-(arr[i-1]%c)+(arr[giveind(i,x,h)]%c))%c
#print(xarr)	
#eprint(xarr)
aarr=list(map(int,input().split()))
carr=list(map(int,input().split()))
#yo=0
for j in range(h-k):
	yo=0
	for i in range(k):
		yo+=((carr[i]%c)*(aarr[-(i+1)]%c))
	aarr.append(yo%c)	
s=0
for i in range(h):
	s=(s%c+aarr[i]%c)%c

p=0
q=s%c

for i in range(h):
	p=((p%c)+(((aarr[i]%c)*(xarr[i]%c))%c))%c
	#ans+=(aarr[i]/s)*(xarr[i])
#print(aarr)
#print(p,q)
p=p%c
q1=modInverse(q,c)
q1=q1%c
ans=(p*q1)%c
#print(p,)
print(ans) 