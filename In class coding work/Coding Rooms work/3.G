a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=abs(a-c)
f=abs(b-d)
if (f%2==1) and (e%2==1):
    print("YES")
elif (f%2==0) and (e%2==0):
    print("YES")
else:
    print("NO")
