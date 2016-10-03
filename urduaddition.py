N=input()
while N>0:
	numbers=[int(str(number)[::-1]) for number in map(int, raw_input().split())]
	print int(str(sum(numbers))[::-1])
	N=N-1
	
