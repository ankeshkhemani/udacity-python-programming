
def find_index(_chocolate_sums,_chocolate):
	min,max=0,len(_chocolate_sums)
	while True:
		index=int((min+max)/2)
		if index==0:
			if _chocolate_sums[index]>=_chocolate:
				return index+1
		if _chocolate_sums[index]<_chocolate:
			min,max=index+1,max
			continue
		elif _chocolate_sums[index]>=_chocolate and _chocolate_sums[index-1]<_chocolate:
			return index+1
		else:
			min,max=min,index-1
			continue
			
boxes=int(raw_input())
chocolates=map(int,raw_input().split())
chocolate_sums=[sum(chocolates[0:i+1]) for i in xrange(boxes)]
tests= int(raw_input())
for test in range(tests):
	chocolate=int(raw_input())
	print find_index(chocolate_sums,chocolate)
