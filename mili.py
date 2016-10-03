def permut(scount):
    if scount ==1:
        return 0
    
    perm=1
    for i in range(1,scount):
        perm=perm*i
    return perm

test= input()
for i in range(test):
    size=input()
    array=map(int,raw_input().split())
    k=array[0]
    count=1
    scount=1
    for j in range(1,size):
        count+=1
        if k==array[j]:
            scount+=1
            if j ==size-1:
                count+=permut(scount)
        else:
            count =count+ permut(scount)
            k=array[j]
            scount=1
    print count
			
