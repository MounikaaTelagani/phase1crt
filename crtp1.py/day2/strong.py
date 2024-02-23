def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum == x:
        return "Strong Number"
    else:
        return "Not a Strong Number"
n=int(input())
print(strong(n))
