#Function to count the pair of socks in a pile of socks

c=[1,2,1,2,3,4]
#h=set(c)

def pair(n,ar):
	set1=set(ar)
	count=0
	pairlist=[]
	paircount=0

	for i in set1:
		for j in ar:
			if i == j:
				count+=1
		pairlist.append(count)
		count=0
	#return pairlist
	for i in pairlist:
		if i == 2:
			paircount+=1

	return paircount

y=pair(6,c)
print(y)
