a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=abs(a-c)
f=abs(b-d)
g=e/2
h=f/2
if e==0 or f==0:
    print("YES")
elif (g>h) or (g<h):
    print("NO")
else:
    print("YES")
