'''# each pizza contains 4 slices here n is no of persons s is no of slices eaten by one person 
n,s=map(int,input().split(" "))
c=n*s
if c%4==0:
    d=c//4
else:
    d=(c//4)+1
print(d)'''

#2nd method
import math
n,s=map(int,input().split(" "))
c=n*s
d=math.ceil(c/4)
print(d)
