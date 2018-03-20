def selectsort(ls):
    for i in range( len(ls)):
        min_index = i
        for j in range(i+1,len(ls)):
            if ls[min_index]>ls[j]:
                min_index = j
        ls[min_index],ls[i]=ls[i],ls[min_index]
    return ls
print(selectsort([2,1,4,5,2,8,9,4,3,5,6]))