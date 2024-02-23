import string
s=input()
s=s.lower()
s1=string.ascii_lowercase
if set(s)==set(s1):
    print("Panagram")
else:
    print("Not a Panagram")
