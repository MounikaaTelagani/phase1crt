def sumofnatural(n):
    if n<1:
        return 1
    else:
        print(n)
        return n+sumofnatural(n-1)
n=int(input())
sum=sumofnatural(n)
print(sum)
