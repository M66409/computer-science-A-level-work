a=int(input())
b=int(input())
c=int(input())
d=int(input())
if abs(a-c)>1 or abs(b-d)>1:
    print("NO")
elif ((abs(a-c)<=1)or(abs(b-d)<=1)):
    print("YES")
