a=list(input().split())
x=int(a[0])
y=float(a[1])

if y>x and x%5==0 :
	ans=float(y-x-0.50)
	yo=str(ans)
	ro=yo.find('.')
	if len(yo[ro+1:])==1:
		#print('hukka')
		yo+='0'
		print(yo)
		#ans=float(yo)
	else:	
		print(round(ans,2))
else:
	yo=str(y)
	ro=yo.find('.')
	if len(yo[ro+1:])==1:
		#print('hukka')
		yo+='0'
		print(yo)	
	else:
		
		print(round(y,2))	