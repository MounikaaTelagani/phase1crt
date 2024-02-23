def rev(n):
    if n<1:
        return 1
    else:
        d=n%10
        print(d)
        return d+rev(n//10)
n=int(input())
