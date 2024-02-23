'''s,s1=map(str,input().split())
print(sorted(list(s)))
print(sorted(list(s)))
if len(s)==len(s1):
    if sorted(list(s))==sorted(list(s1)):
        print("True")
    else:
        print("False")
else:
    print("False")'''


d={}
for i in range(2):
    k,v=map(str,input().split())
    d[k]=v
print(d)
l=list(d.values())
if len(l[0])==len(l[1]):
    if sorted(list(l[0]))==sorted(list(l[1])):
        print("True")
    else:
        print("False")
else:
    print("False")
