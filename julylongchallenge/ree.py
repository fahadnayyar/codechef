data=[[0 for i in range(5001)] for i in range(5001)]
#print("bhag")
#

for i in range(5001):

	for j in range(i+1):
		if (i==j):
			data[i][j]=1
		elif j ==0:
			#j==0:
			data[i][j]=1
		else:	
			data[i][j]=(data[i-1][j-1]%1000000006+data[i-1][j]%1000000006)%1000000006

def select(n,k):
	return data[n][k]


if __name__ == '__main__':
	
	t=int(input())

	for z in range(t):

		[n,k]=[int(i) for i in input().split()]
		arr=[int(i) for i in input().split()]

		arr.sort()

		mega=1

		for i in range(n):

			power=select(n-1,k-1)

			if i>=k-1:
				power-=select(i-1+1,k-2+1)

			if i<=n-k:
				power-=select(n-i-2+1,k-2+1)

			mega=((mega%1000000007)*(pow(arr[i],power,1000000007)))%1000000007
			#print(mega)
		print(mega%1000000007)