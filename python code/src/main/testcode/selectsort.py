def selectsort(ls):
    len_ = len(ls)
    for i in  range(len_):
        min_index = i
        for j in range(i+1,len_):
            if ls[min_index]>ls[j]:
                min_index = j
        ls[i],ls[min_index]=ls[min_index],ls[i]
    return ls

print (selectsort([1,5,2,2,6,9,3]))
