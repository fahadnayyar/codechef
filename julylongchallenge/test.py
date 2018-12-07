from random import *
arr= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
t=20
print(t)
n=100000
#print(n)
for j in range(t):

	for i in range(n):
		print(arr[randint(0,25)],end="")
	print()	