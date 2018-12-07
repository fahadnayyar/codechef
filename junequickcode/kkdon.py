from math import log
from math import ceil
from math import inf
class vertex:
	def __init__(self,freq,num):
		self.freq=freq
		self.num=num

	def maxi(self,b):
		if(self.freq>b.freq):
			return self
		else:
			return b
class SegmentTree:
	def __init__(self,arr,n):
		self.arr=arr
		self.l=self.givesize(n)
		self.segmentarr=[0]*(self.l)
		self.maxarr=[]
		for i in range(self.l):
			self.maxarr.append(vertex(-1,-1))
		#self.maxarr=[0]*self.givesize(n)
		self.construct(0,n-1,0,self.arr)
		#rint(self.segmentarr)

	def construct(self,low,high,pos,arr):
		if(low==high):
			self.segmentarr[pos]=arr[low]
			self.maxarr[pos].freq=arr[low]
			self.maxarr[pos].num=low
			return
		mid=low+(high-low)//2
		self.construct(low,mid,2*pos+1,arr)
		self.construct(mid+1,high,2*pos+2,arr)
		self.segmentarr[pos]=self.segmentarr[2*pos+1]+self.segmentarr[2*pos+2]
		self.maxarr[pos]=self.maxarr[2*pos+1].maxi(self.maxarr[2*pos+2])
	
	def givesize(self,n):
		x=ceil(log(n)/log(2))
		self.size=2*(2**(x))-1
		return self.size 

	def rangeminimum(self,ql,qh,l,h,pos):
		if(ql>h or qh<l):
			ans=[]
			ans.append(0)
			ans.append(vertex(-1,-1))
			return ans
		if(ql<=l and qh>=h):
			ans=[]
			ans.append(self.segmentarr[pos])
			ans.append(self.maxarr[pos])
			return ans
		mid=(l+h)//2
		left=self.rangeminimum(ql,qh,l,mid,2*pos+1)
		right=self.rangeminimum(ql,qh,mid+1,h,2*pos+2)
		ans=[]
		ans.append(left[0]+right[0])
		ans.append(left[1].maxi(right[1]))
		return ans
	
	def updatestart(self,i,new):
		diff=new-self.arr[i]
		self.arr[i]=new
		self.update(0,len(self.arr)-1,i,diff,0)
		#print("update",self.segmentarr)

	def update(self,l,h,i,diff,pos):
		if(i<l or i>h):
			return 
		if(l==h):
			self.segmentarr[pos]+=diff
			self.maxarr[pos].freq+=diff
			return
		mid=l+(h-l)//2
		self.update(l,mid,i,diff,2*pos+1)
		self.update(mid+1,h,i,diff,2*pos+2)
		self.segmentarr[pos]=self.segmentarr[2*pos+1]+self.segmentarr[2*pos+2]
		self.maxarr[pos]=self.maxarr[2*pos+1].maxi(self.maxarr[2*pos+2])

def search(s,l,r,value,n):
	a=l
	b=r
	#print(value,a,b)
	while(a<=b):
		mid=(a+b)//2
		if(s.rangeminimum(l,mid,0,n-1,0)[0]>=value):
			b=mid-1
		else:
			a=mid+1
	return a
def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)
if(__name__=='__main__'):
	t=int(input())
	for i in range(t):
		a=[int(i) for i in input().split()]
		n=a[0]
		q=a[1]
		a=[int(i) for i in input().split()]
		b=SegmentTree(a,n)
		for j in range(q):
			x=[int(i) for i in input().split()]
			c=x[0]
			if(c==1):
				l=x[1]-1
				r=x[2]-1
				ans=b.rangeminimum(l,r,0,n-1,0)
				mode=ans[1].num+1
				ans=ans[0]
				if(ans%2==0):
					w=search(b,l,r,ans//2,n)
					e=search(b,l,r,(ans//2)+1,n)		
					med=(w+e)//2
				else:
					w=search(b,l,r,(ans+1)//2,n)
					med=w
				med+=1
				if(mode>med):
					p=gcd(mode,med)
				else:
					p=gcd(med,mode)
				#print(med,mode)
				pro=(med//p)*(mode)
				print(pro)
			else:
				ind=x[1]-1
				x=x[2]
				b.updatestart(ind,x)