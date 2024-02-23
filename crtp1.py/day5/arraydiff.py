l,d=map(int,input().split())
l1=list(map(int,input().split()))
for i in l1:
    for j in l1:
        if i-j ==d:
            flag=1
x=True if flag==1 else Flase
print(x)

    
