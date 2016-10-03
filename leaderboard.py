N=input()
rows=[]
M=N
while N>0:
    columns=map(str, raw_input().split())
    row=[""]
    FoundScore=False
    for i in range(len(columns)):
        if columns[i]=="20" or columns[i]=="5":
            FoundScore=True
        if FoundScore==True:
            row.append(columns[i])
        else:
            row[0]=row[0]+" "+columns[i]
    rows.append(row)
Leaderboard=[{Rank=1,Name="",EE=0,I1=0,TTT=0,Score=0]
for row in rows:
    if row[0] not in Leaderboard("Name"):
             Leaderboard.append(
             
