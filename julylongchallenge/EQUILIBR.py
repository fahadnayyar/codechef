def hcf(a, b):
	while (a != b):
		if (a > b):
			a = a - b
		else:
			b = b - a
	return a

def modInverse(a, m) :
	m0 = m
	y = 0
	x = 1
 
	if (m == 1) :
		return 0
 
	while (a > 1) :
 
        # q is quotient
		q = a // m
 
		t = m
 
        # m is remainder now, process
        # same as Euclid's algo
		m = a % m
		a = t
		t = y
 
        # Update x and y
		y = x - q * y
		x = t
 
 
    # Make x positive
	if (x < 0) :
		x = x + m0
 
	return x
 
 
n=int(input())
k=int(input())
p=1000000007
yo = pow(2,n-1)
ro = (yo - n)
gc = gcd (yo,ro)
pp =  ro//gc
qq =  yo//gc		
#print(yo,ro)
bo = modInverse(yo,p)
ans = (pp%p*bo%p)%p
print(ans) 