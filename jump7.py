i=1
while i<101:
	if i/7==0 or i%10==7 or i//10==7:
		i+=1
		continue
	else:
		print(i)
		i+=1

