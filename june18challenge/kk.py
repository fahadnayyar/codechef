class graph:
	def _init_(self,m,n,arr):
		self.m=m
		self.n=n
		self.arr=arr
	def giveneighbour(self,i,j):
		a=[]
		if(i+1>=0 and i+1<self.m and j>=0 and j< self.n):
			a.append([i+1,j])
		if(i-1>=0 and i-1<self.m and j>=0 and j< self.n):
			a.append([i-1,j])
		if(i>=0 and i<self.m and j+1>=0 and j+1< self.n):
			a.append([i,j+1])
		if(i>=0 and i<self.m and j-1>=0 and j-1< self.n):
			a.append([i,j-1])
		return a
	def bfs(self,a,b):
		booleanarr=[]
		for i in range(n):
			y=[]
			for j in range(m):
				y.append(False)
			booleanarr.append(y)
		maxi=0
		for i in range(n):
			for j in range(m):
				if(self.arr[i][j]==a or self.arr[i][j]==b):
					if(booleanarr[i][j]==False):
						a=self.bfsvisit(a,b,i,j,booleanarr)
						if(a>maxi):
							maxi=a
		return maxi
	def bfsvisit(self,a,b,x,y,arr):
		count=1
		arr[x][y]=True
		queue=[]
		queue.append([x,y])
		while queue!=[]:
			el=queue.pop(0)
			neighbour=self.giveneighbour(el[0],el[1])
			while neighbour!=[]:
				n=neighbour.pop(0)
				i=n[0]
				j=n[1]
				if(self.arr[i][j]==a or self.arr[i][j]==b):
					if(arr[i][j]==False):
						arr[i][j]=True
						queue.append([i,j])			
						count+=1
		return count

if __name__=='__main___':
	a=[int(i) for i in input().split()]
	n=a[0]
	m=a[1]
	x=[[int(j) for j in input().split()] for i in range(n)]
	b=[]
	for i in range(n):
		for j in range(m):
			if(x[i][j] not in b):
				b.append(x)
	l=len(b)
	g=graph(n,m,x)
	ans=0
	if(l==1):
		print(n*m)
	else:
		for i in range(l-1):
			for j in range(i+1,l):
				a=g.bfs(i,j)
				if(ans<a):
					ans=a
		print(ans)