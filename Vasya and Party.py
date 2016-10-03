

nm=map(int,raw_input().split())
n=nm[0]
m=nm[1]
groups=[[]]
games=1
smartest_count=[]
smartest=[]
array=map(int,raw_input().split())
def build_groups(_relation):
	notfound=True
	if groups[0]==[]:
		groups[0]=([_relation[0],_relation[1]])
		if array[_relation[0]] == array[_relation[1]]:
			smartest_count.append(2)
			smartest.append(_relation[0])
		elif array[_relation[0]] > array[_relation[1]]:
			smartest_count.append(1)
			smartest.append(_relation[0])
		elif array[_relation[1]] > array[_relation[0]]:
			smartest_count.append(1)
			smartest.append(_relation[1])
	else:
		for groupno in xrange(len(groups)):
			leftout=-1
			if _relation[0] in groups[groupno] and _relation[1] not in groups[groupno]:
				leftout=_relation[1]
				notfound=False
			elif _relation[1] in groups[groupno] and _relation[0] not in groups[groupno]:
				leftout=_relation[0]
				notfound=False
			elif _relation[1] in groups[groupno] and _relation[0] in groups[groupno]:
				notfound=False
			if leftout!=-1:
				groups[groupno].append(leftout)
				if array[leftout] > array[smartest[groupno]]:
					smartest[groupno]=leftout
				elif array[leftout] == array[smartest[groupno]]:
					smartest_count[groupno] +=1
			if leftout !=-1 and groupno < len(groups)-1:
				for group2 in xrange(groupno+1,len(groups)):
					if array[leftout] in groups[group2]:
						groups[groupno].append(groups[group2])
						if array[smartest[groupno]] < array[smartest[group2]]:
							smartest[groupno]=smartest[group2]
							smartest_count[groupno]=smartest_count[group2]
						elif array[smartest[groupno]] == array[smartest[group2]]:
							smartest_count[groupno]=smartest_count[groupno]+smartest_count[group2]
						groups[group2].pop()
						smartest[group2].pop()
						smartest_count[group2].pop()
						break
			if notfound==True and groupno==len(groups)-1:
				groups.append([_relation[0],_relation[1]])
				if array[_relation[0]] == array[_relation[1]]:
					smartest_count.append(2)
					smartest.append(_relation[0])
				elif array[_relation[0]] > array[_relation[1]]:
					smartest_count.append(1)
					smartest.append(_relation[0])
				elif array[_relation[1]] > array[_relation[0]]:
					smartest_count.append(1)
					smartest.append(_relation[1])
					
for i in xrange(m):
	relation=map(int,raw_input().split())
	relation=[relation[0]-1,relation[1]-1]
	build_groups(relation)
for group_index in xrange(len(groups)):
        games=games*smartest_count[group_index]
print games%(10^9+7)
print groups

