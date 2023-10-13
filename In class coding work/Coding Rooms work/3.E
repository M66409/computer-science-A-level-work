a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=a+b
f=c+d
if (e%2==0) and (f%2==0):
    print("YES")
elif (e%2==1) and (f%2==1):
    print("YES")
else:
    print("NO")
