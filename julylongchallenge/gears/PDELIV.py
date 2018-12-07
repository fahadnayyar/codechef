from copy import deepcopy
yoar = list(map(int,input().split()))
n=yoar[0]
m=yoar[1]
cost = []
location =[]
for i in range(n):
	yoar = list(map(int,input().split()))
	li=yoar[0]
	ci=yoar[1]
	location.append(li)
	cost.append(ci)
for i in range(m):
	yoar = list(map(int,input().split()))
	qi=yoar[0]
	ki=yoar[1]
	copylocation = deepcopy(location)
	for j in range(2,ki+2):
		copylocation[yoar[j]-1]=-1
	mini = 10**20
	for j in range(0,n):
		if copylocation[j]!=-1:
			curmini = (location[j]-qi)**2 + cost[j]
			if curmini<mini:
				mini=curmini
	print(mini)			
