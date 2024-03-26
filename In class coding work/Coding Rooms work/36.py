x=int(input())
a=x//100
b=(x//10)%10
c=x%10
if (a>b) or a>c or b>c:
    print("NO")
else:
    print("YES")
