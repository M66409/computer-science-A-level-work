a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=abs(a-c)%3
f=abs(b-d)%3
if ((e>1)^(f>1)) and ((e<=1)^(f<=1)):
    print("YES")
else:
    print("NO")
