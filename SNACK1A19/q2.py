def func(n):
	ans=0
	if(n):
		ro=n & -(n)
		nhob=n + int(ro)
		rop=n ^ int(nhob)
		rop=(int(rop) / int(ro))
		rop= int(rop) >> 2
		ans=nhob | rop
	return ans
def no_of_ones(n):
	s=bin(n)[2:]
	l=len(s)
	c=0
	#print(s)
	for i in range(l):
		if(s[i]=="1"):
			c+=1
	return c
t=int(input())
for i in range(t):
	x=[int(i) for i in input().split()]
	a=x[0]
	b=x[1]
	c=x[2]
	ab=bin(a)[2:]
	bb=bin(b)[2:]
	cb=bin(c)[2:]
	al=len(ab)
	bl=len(bb)
	ao=no_of_ones(a)
	minia="1"*(ao)
	miniaint=int(minia,2)
	count=0
	while miniaint<(1<<(al+1)):
		newb=c-miniaint
		if(newb>0 and newb<(1<<(bl+1)) and no_of_ones(newb)==no_of_ones(b)):
			#print(miniaint,newb)
			count+=1
		if(newb<0):
			break
		miniaint=func(miniaint)
	print(count)