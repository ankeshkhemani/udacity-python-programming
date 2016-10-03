notprime=[]
isprime=[]
def printprime(m,n):
	for i in range(m,n+1):
		if i in notprime:
			continue
		if i in isprime:
			print i
			continue
		if i == 1:
			continue
		prime=True
		for j in isprime:
			if i%j==0:
				prime=False
				notprime.append(i)
				break
			if j>i/2:
				break
		if prime==True:
			isprime.append(i)
			print i


N=input()
while N>0:
	N-=1
	mn=map(int,raw_input().split())
	printprime(mn[0],mn[1])
