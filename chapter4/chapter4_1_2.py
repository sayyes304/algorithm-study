n=int(input())
count=0

for i in range(0,n+1):
    i=str(i)
    for j in range(60):
        j=str(j)
        for k in range(60):
            k=str(k)
            if i[0]=='3' or i[-1]=='3' or j[0]=='3' or j[-1]=='3' or k[0]=='3' or k[-1]=='3':
                count+=1

print(count)