'''def factorial(n):
    if n ==0:
        return 1
    else:
        return n* factorial(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=factorial(int(i))
    if sum ==x:
        return "Strong Numbers"
    else:
        return "Not a Strong Number"
x=int(input())
print(strong(x))'''


def factorial(n):
    if n ==0:
        return 1
    else:
        return n* factorial(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=factorial(int(i))
    if sum ==x:
        print(x)
a,b=int(input()),int(input())
for i in range(a,b+1):
    strong(i)
