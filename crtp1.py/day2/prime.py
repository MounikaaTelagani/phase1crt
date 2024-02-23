'''n=int(input())
c=0
for i in range (1,n+1):
        if n%i==0:
            c+=1
if c==2:
    print("it's a prime number")
else:
    print("not a prime number")'''
            
n=int(input())
for i in range (2,n):
        if n%i==0:
           print("not Prime number")
           break      
else:
        print("prime number")
