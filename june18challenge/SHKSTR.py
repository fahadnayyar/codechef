piclass TrieNode:
	
	def __init__(self):
		self.children=[None]*26
		self.is_end_of_word=False
		#self.count=0
		#self.leaves=[]
		self.mins=''
class Trie:
	def __init__(self):
		self.root=TrieNode()
	def _giveInd(self,ch):
		return ord(ch)-ord('a')
	def insert(self,key,l):
		leafs=key
		yo=self.root
		for i in range(l):
			ind=self._giveInd(key[i])
			#print(ind)	
			if  yo.children[ind]==None:
				yo.children[ind]=TrieNode()
			#yo.leaves.append(leaf)	
			if yo.mins=='':
				yo.mins=leafs;
			yo.mins=min(yo.mins,leafs)
			#yo.count+=1
			yo=yo.children[ind]	
		if yo.mins=='':
				yo.mins=leafs;
		yo.mins=min(yo.mins,leafs)
		#yo.leaves.append(leaf)
		#yo.count+=1
		yo.is_end_of_word=True
	def search(self,key,l):
		yo=self.root
		for i in range(l):
			ind=self._giveInd(key[i])
			if yo.children[ind]==None:
				return False
			yo=yo.children[ind]
		return (yo !=None) and (yo.is_end_of_word)
	def givecount(self,key,l):
		yo=self.root
		for i in range(l):
			ind=self._giveInd(key[i])
			if yo.children[ind]==None:
				return yo.mins
			yo=yo.children[ind]
		if yo==None:
			return yo.mins
		else:
			return yo.mins
 
 
 
 
 
class query:
	def __init__(self,r,query,ind):
		self.ind=ind
		self.query=query
		self.r=r
n=int(input())
sarr=[]
for i in range(n):
	si=input()
	sarr.append(si)
q=int(input())
qarr=[]
for i in range(q):
	yoarr=list(input().split())	
	ri=int(yoarr[0])-1
	qi=yoarr[1]
	queryy=query(ri,qi,i)
	qarr.append(queryy)
qarr.sort(key =lambda query:(query.r))
#print("sorted")
prev=-1
trie=Trie()
ansarr=[]
for i in range(q):
	ansarr.append("")
for i in qarr:
	if i.r>prev:
		for j in range(prev+1,i.r+1):
			#print(j)
			trie.insert(sarr[j],len(sarr[j]))
			prev=i.r
		ar=trie.givecount(i.query,len(i.query))
	
		ansarr[i.ind]=ar
 
	else:
				
		ar=trie.givecount(i.query,len(i.query))
 
		ansarr[i.ind]=ar
	
for i in range(q):
	print(ansarr[i])			
 