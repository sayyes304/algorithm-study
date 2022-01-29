n,m,k=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
sum=0
count=0
for i in range(m):
    if count==k:
        sum+=nlist[-2]
        count=0
    else:
        sum+=nlist[-1]
        count+=1
print(sum)




