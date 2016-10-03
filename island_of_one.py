def dfs(arr,mark,i,j):
    for ii in range(i-1,i+2):
        for jj in range(j-1,j+2):
            try:
                if ii>-1 and jj>-1:
                    if arr[ii][jj] ==1 and  mark[ii][jj]==0:
                        mark[ii][jj]=1
                        dfs(arr,mark,ii,jj)
                    else:
                        mark[ii][jj]=1

            except IndexError:
                pass
    return 0

def count_islands(m,n,arr):
    mark=[[]]
    for i in range(m):
        if i == 0:
            mark[0]=[0 for cells in arr[i]]
        else:
            mark.append([0 for cells in arr[i]])
    island_count = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] and mark[i][j]==0:
                mark[i][j] =1
                island_count+=1
                dfs(arr,mark,i,j)
            mark[i][j]=1            
    return island_count

def take_test_case():
    arr=[[]]
    mn=map(int, raw_input().split())
    m,n=mn[0],mn[1]
    for i in range(m):
        row=map(int,raw_input().split())
        if i == 0:
            arr[0]=row
        else:
            arr.append(row)
    print count_islands(m,n,arr)

test_count=input()
while test_count>0:
    take_test_case()
    test_count-=1
