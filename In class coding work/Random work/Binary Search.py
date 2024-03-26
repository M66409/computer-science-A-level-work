nums=[0,1,2,3,4,5,6,7,8,9,10,12,14,16,23,25,36,47,58]
num=int(input("number to search for:"))
found=False
fpointer=0
lpointer=len(nums)-1
while found==False:
    midpoint=(fpointer+lpointer)//2
    if nums[midpoint]==num:
        found=True
        print(midpoint)
    elif nums[midpoint]>num:
        lpointer=midpoint-1
    else:fpointer=midpoint+1
