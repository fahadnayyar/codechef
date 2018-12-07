arrr=["f","r","i","e","z","a",]
t=int(input())
for w in range(t):
	s=input()
	l=len(s)
	i=0
	ans=[]
	while i<l:
		if s[i] in arrr:
			j=i+1
			count=1
			while True:
				if j>=l:
					i=j
					break
				if s[j] not in arrr :
					i=j
					break
				else:
					j+=1
					count+=1
			ans.append(count)			
		else:
			j=i+1
			count=1
			while True:
				if j>=l:
					i=j
					break
				if s[j] in arrr :
					i=j
					break
				else:
					j+=1
					count+=1
			ans.append(count)
	for i in ans:
		print(i,end="")
	print()						