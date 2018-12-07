t = int(input())
for w in range(t):
	s1 = input()
	s2 = input()
	
	s1a = s1[0] + s1[1] + s1[2]
	s1b = s2[0] + s2[1] + s2[2]

	s2a = s1[0] + s1[2] + s1[1]
	s2b = s2[0] + s2[2] + s2[1]

	s3a = s1[1] + s1[0] + s1[2]
	s3b = s2[1] + s2[0] + s2[2]

	s4a = s1[1] + s1[2] + s1[0]
	s4b = s2[1] + s2[2] + s2[0]

	s5a = s1[2] + s1[0] + s1[1]
	s5b = s2[2] + s2[0] + s2[1]

	s6a = s1[2] + s1[1] + s1[0]
	s6b = s2[2] + s2[1] + s2[0]
	flag = 0
	if (s1a[0]=="b" or s1b[0]=="b") and (s1a[1]=="o" or s1b[1]=="o") and (s1a[2]=="b" or s1b[2]=="b"):
		flag = 1
	elif (s2a[0]=="b" or s2b[0]=="b") and (s2a[1]=="o" or s2b[1]=="o") and (s2a[2]=="b" or s2b[2]=="b"):	
		flag = 1
	elif (s3a[0]=="b" or s3b[0]=="b") and (s3a[1]=="o" or s3b[1]=="o") and (s3a[2]=="b" or s3b[2]=="b"):	
		flag = 1
	elif (s4a[0]=="b" or s4b[0]=="b") and (s4a[1]=="o" or s4b[1]=="o") and (s4a[2]=="b" or s4b[2]=="b"):	
		flag = 1
	elif (s5a[0]=="b" or s5b[0]=="b") and (s5a[1]=="o" or s5b[1]=="o") and (s5a[2]=="b" or s5b[2]=="b"):	
		flag = 1
	elif (s6a[0]=="b" or s6b[0]=="b") and (s6a[1]=="o" or s6b[1]=="o") and (s6a[2]=="b" or s6b[2]=="b"):	
		flag = 1							
	if flag==1:
		print("yes")
	else:
		print("no")			