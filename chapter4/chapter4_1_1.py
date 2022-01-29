n=int(input())
x,y=1,1
go=input().split()

for i in go:
    if i=="R":
        y+=1
        if x>n:
            y-=1
    elif i=="L":
        y-=1
        if y==0:
            y+=1
    elif i=="U":
        x-=1
        if x==0:
            x +=1
    else:
        x +=1
        if x >n:
            x-=1

print(x,y)
