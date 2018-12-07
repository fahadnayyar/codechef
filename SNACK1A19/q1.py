class dsu:
	def __init__(self,n):
		self.arr=[]
		self.size=[]
		for i in range(n):
			self.arr.append(i)
			self.size.append(1)
	def find(self,i):
		if(self.arr[i]==i):
			return i
		else:
			self.arr[i]=self.find(self.arr[i])
			return self.arr[i]
	def union(self,i,j):
		fa=self.find(i)
		fb=self.find(j)
		if(fa==fb):
			return
		else:
			if(self.size[fa]>self.size[fb]):
				self.size[fa]+=self.size[fb]
				self.arr[fb]=fa
			else:
				self.size[fb]+=self.size[fa]
				self.arr[fa]=fb
def gcd(a,b):
	while(b!=0):
		r=a%b
		a=b
		b=r
	return a
primefactors=[0]*(50)
primefactors[0]=[1]
primefactors[1]=[2]
primefactors[2]=[3]
primefactors[3]=[2]
primefactors[4]=[5]
primefactors[5]=[2,3]
primefactors[6]=[7]
primefactors[7]=[2]
primefactors[8]=[3]
primefactors[9]=[2,5]
primefactors[10]=[11]
primefactors[11]=[2,3]
primefactors[12]=[13]
primefactors[13]=[2,7]
primefactors[14]=[3,5]
primefactors[15]=[2]
primefactors[16]=[17]
primefactors[17]=[2,3]
primefactors[18]=[19]
primefactors[19]=[2,5]
primefactors[20]=[3,7]
primefactors[21]=[2,11]
primefactors[22]=[23]
primefactors[23]=[2,3]
primefactors[24]=[5]
primefactors[25]=[2,13]
primefactors[26]=[3]
primefactors[27]=[2,7]
primefactors[28]=[29]
primefactors[29]=[2,3,5]
primefactors[30]=[31]
primefactors[31]=[2]
primefactors[32]=[3,11]
primefactors[33]=[2,17]
primefactors[34]=[5,7]
primefactors[35]=[2,3]
primefactors[36]=[37]
primefactors[37]=[2,19]
primefactors[38]=[3,13]
primefactors[39]=[2,5]
primefactors[40]=[41]
primefactors[41]=[2,3,7]
primefactors[42]=[43]
primefactors[43]=[2,11]
primefactors[44]=[3,5]
primefactors[45]=[2,23]
primefactors[46]=[47]
primefactors[47]=[2,3]
primefactors[48]=[7]
primefactors[49]=[2,5]
arr=[]
par=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
for i in range(50):
	x=[1]*(50)
	arr.append(x)
for i in range(50):
	for j in range(50):
		arr[i][j]=gcd(i+1,j+1)
t=int(input())
for i in range(t):
	n=int(input())
	a=[int(i) for i in input().split()]
	flag1=0
	ds=dsu(n)
	for i in range(n):
		for j in range(i+1,n):
			if(a[i]!=a[j] and arr[a[i]-1][a[j]-1]==1):
				ds.union(i,j)
	rep=ds.find(0)
	for i in range(1,n):
		if(rep!=ds.find(i)):
			flag1=1
			break
	if(flag1==0):
		print(0)
		for i in range(n):
			print(a[i],end=" ")
		print()
	elif(n==1):
		print(0)
		print(a[0])
	else:
		print(1)
		primes=[]
		for j in a:
			for k in primefactors[j-1]:
				if(k not in primes):
					primes.append(k)
		for j in par:
			if j not in primes:
				a[0]=j
				break
		for j in a:
			print(j,end=" ")
		print()