n,m=map(int,input().split())
nlist=[]
for i in range(n):
    newlist = list(map(int,input().split()))
    newlist.sort()
    nlist.append(newlist[0])
nlist.sort()
print(nlist[-1])


