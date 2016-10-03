output=[[]]
def hcount(index,arr):
    xcount=0
    ocount=0
    for i in range(index):
        xcounter=0
        ocounter=0
        for j in range(index):
                if arr[i][j]=="o":
                    ocounter +=1
                    xcounter =0
                if arr[i][j]=="x":
                    xcounter +=1
                    ocounter =0
                if xcounter>2:
                    xcount+=1
                if ocounter>2:
                    ocount+=1
    return [xcount,ocount]

def vcount(index,arr):
    xcount=0
    ocount=0
    for j in range(index):
        xcounter=0
        ocounter=0
        for i in range(index):
                if arr[i][j]=="o":
                    ocounter +=1
                    xcounter =0
                if arr[i][j]=="x":
                    xcounter +=1
                    ocounter =0
                if xcounter>2:
                    xcount+=1
                if ocounter>2:
                    ocount+=1
    return [xcount,ocount]

def fdcount(index,arr):
    m=index-3
    n=0
    xcount=0
    ocount=0
    while n<=index-3:
        i,j,xcounter,ocounter=m,n,0,0
        while i<index and j<index:
            if arr[i][j]=="o":
                ocounter +=1
                xcounter =0
            if arr[i][j]=="x":
                xcounter +=1
                ocounter =0
            if xcounter>2:
                xcount+=1
            if ocounter>2:
                ocount+=1
            i+=1
            j+=1
        if i==index and j!=index:
            m=m-1
        if j==index:
            n=n+1
    return [xcount,ocount]

def bdcount(index,arr):
    m=2
    n=0
    xcount=0
    ocount=0
    while n<=index-3:
        i,j,xcounter,ocounter=m,n,0,0
        while i>=0 and j<index:
            if arr[i][j]=="o":
                ocounter +=1
                xcounter =0
            if arr[i][j]=="x":
                xcounter +=1
                ocounter =0
            if xcounter>2:
                xcount+=1
            if ocounter>2:
                ocount+=1
            i-=1
            j+=1
        if i==-1 and j!=index:
            m=m+1
        if j==index:
            n=n+1
    return [xcount,ocount]
    
def score_calc(index,arr):
    h=hcount(index,arr)
    v=vcount(index,arr)
    fd=fdcount(index,arr)
    bd=bdcount(index,arr)
    return [h[0]+v[0]+fd[0]+bd[0],h[1]+v[1]+fd[1]+bd[1]]

def take_test():
    arr=[[]]
    index=int(raw_input())
    for i in range(index):
        input_string=raw_input().split()
        if i == 0:
            arr[0]=[cell for cell in input_string]
        else:
            arr.append([cell for cell in input_string])
    output.append(score_calc(index,arr))

test_count=int(raw_input())
for test_number in range(test_count):
    take_test()

for test_number in range(test_count):
    print ("%d %d" % (output[test_number+1][0], output[test_number+1][1]))
