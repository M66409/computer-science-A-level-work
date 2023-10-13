a=int(input())
b=int(input())
if a in (1,3,5,7,8,10,12):
    if a==12 and b==31:
        print(1)
        print(1)
    elif b<31:
        print(a)
        print(b+1)
    else:
        print(a+1)
        print(1)
elif a in (4,6,9,11):
    if b<30:
        print(a)
        print(b+1)
    else:
        print(a+1)
        print(1)
elif a==2:
    if b<28:
        print(a)
        print(b+1)
    else:
        print(a+1)
        print(1)
