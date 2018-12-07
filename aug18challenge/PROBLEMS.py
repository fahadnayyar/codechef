class problem:
	def __init__(self,diff,ind):
		self.diff=diff
		self.ind=ind
class subprob:
	def __init__(self,score,num):
		self.num=num
		self.score=score
yoar = list(map(int,input().split()))
p = yoar[0]
s = yoar[1]
parr = [0]*(p)
for j in range(p):
	score = list(map(int,input().split()))
	nums = list(map(int,input().split()))
	subprobar = [0]*(s)
	#print(subprobar)
	for i in range(s):
		#print(i,s)
		subprobar[i]=subprob(score[i],nums[i])
	subprobar.sort(key = lambda subprob:subprob.score)
	diff=0
	for i in range(s-1):
		if subprobar[i].num>subprobar[i+1].num:
			diff+=1
	parr[j]=problem(diff,j)
	#print(parr[i].diff,parr[i].ind)

parr.sort(key = lambda problem:problem.diff)			
for i in parr:
	print(i.ind+1)