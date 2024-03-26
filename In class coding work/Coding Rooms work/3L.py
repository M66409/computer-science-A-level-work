a=int(input())
b=int(input())
if a==0 and b>0:
    print("no solution")
elif a==0 and b==0:
    print("many solutions")
elif(b/a!=b//a):
    print("no solution")
else:
    print(int(b//a))
