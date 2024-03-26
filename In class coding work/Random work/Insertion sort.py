def insertion_sort(tosort):
    for i in range(1,len(tosort)):
        current=tosort[i]
        index=i
        while index >0 and tosort[index-1]>current:
            tosort[index]=tosort[index-1]
            index=index-1
        tosort[index]=current
    return tosort

items = [16,2,325,123,63,8,999]
print(insertion_sort(items))
