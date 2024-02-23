ns,cd=map(int,input().split(" "))
if cd >= ns:
    np=0
else :
    c=ns-cd
    if c%4==0:
        np=c//4
    else:
         np=(c//4)+1
print(np)
