class disjointsets:
	def __init__(self,n):
		self.arr=[0]*(n)
		self.size=[1]*(n)
		for i in range(n):
			self.arr[i]=i
	def find(self,i):
		if(self.arr[i]==i):
			return i
		else:
			self.arr[i]=self.find(self.arr[i])
			return self.arr[i]
			#return self.find(self.arr[i])
	def union(self,i,j):
		f1=self.find(i)
		f2=self.find(j)
		#print(f1,f2,self.size[f1],self.size[f2])
		if(f1==f2):
			return
		else:
			if(self.size[f1]>self.size[f2]):
				self.arr[f2]=f1
				self.size[f1]+=self.size[f2]	
			else:
				self.arr[f1]=f2
				self.size[f2]+=self.size[f1]
def gcd(a,b):
	if(a<b):
		temp=a
		a=b
		b=temp
	while(b>0):
		r=b%a
		a=b
		b=r
	return a
if(__name__=='__main__'):
	a=[int(i) for i in input().split()]
	n=a[0]
	m=a[1]
	d1=disjointsets(n)
	d2=disjointsets(n)
	flag=[0]*(n)
	arr=[-1]*(n)
	colorarr=[0]*(n)
	teeth=[int(i) for i in input().split()]
	#print(teeth)
	for i in range(m):
		a=[int(i) for i in input().split()]
		if(a[0]==1):
			teeth[a[1]-1]=a[2]
		elif(a[0]==2):
			f1=d1.find(a[1]-1)
			f2=d1.find(a[2]-1)
			if(f1==f2):
				c1=d2.find(a[1]-1)
				c2=d2.find(a[2]-1)
				x=a[1]-1
				y=a[2]-1
				#d1.union(x,y)
				if(c1==c2):
					if x!=y:
						flag[f1]=1
			else:
				fl1=flag[f1]
				fl2=flag[f2]
				x=a[1]-1
				y=a[2]-1
				neighx=arr[x]
				neighy=arr[y]
				d1.union(x,y)
				if(neighx==neighy and neighx==-1):
					colorarr[x]=1
					colorarr[y]=2
				elif(neighx==-1):
					c=colorarr[d2.find(neighy)]
					d2.union(x,neighy)
					colorarr[d2.find(x)]=c
				elif(neighy==-1):
					c=colorarr[d2.find(neighx)]
					d2.union(neighx,y)
					colorarr[d2.find(y)]=c
				else:
					c1=colorarr[d2.find(x)]
					c2=colorarr[d2.find(neighx)]
					d2.union(neighx,y)
					d2.union(neighy,x)
					colorarr[d2.find(x)]=c1
					colorarr[d2.find(y)]=c2
				arr[x]=y
				arr[y]=x
				if(fl1==1 or fl2==1):
					flag[d1.find(x)]=1
		else:
			p=teeth[a[1]-1]*(a[3])
			q=teeth[a[2]-1]
			g=gcd(p,q)
			p=p//g
			q=q//g
			f1=d1.find(a[1]-1)
			f2=d1.find(a[2]-1)
			if(f1==f2 and flag[f1]==0):
				c1=d2.find(a[1]-1)
				c2=d2.find(a[2]-1)
				s=str(p)+'/'+str(q)
				if(c1==c2):
					print(s)
				else:
					print('-'+s)
			else:
				print(0)