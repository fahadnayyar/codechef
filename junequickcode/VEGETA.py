# def give_count_primes(n):
# 	if n<2:
# 		return 0
# 	else:
# 		boolarr=[]
# 		for i in range()



maxa=1000001
arrr=[]
for i in range(maxa):
	arrr.append(0)
#arrr[1]=1
for i in range(1,maxa):
	arrr[i]=i	
for i in range(4,maxa,2):
	arrr[i]=2
i=3
while i*i<maxa:
	if arrr[i]==i:
		j=i*i
		while j<maxa:
			if arrr[j]==j:
				arrr[j]=i
			j+=i			
	i+=1
def give_count_primes(arrr,x):
	count=[]
	while x!=1:
		count.append(arrr[x])
		x=x//arrr[x]
	return	len(set(count))
t=int(input())
for w in range(t):
	yoar=list(map(int,input().split()))
	n=yoar[0]
	m=yoar[1]
	anscount=0
	for i in range(n,m):
		#print(i,give_count_primes(arrr,i))
		anscount+=give_count_primes(arrr,i)
	print(anscount)		