def bubblesort(ls):
    len_ = len(ls)
    for i in  range(len_):
        for j in  range(0,len(ls)-1-i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls

print (bubblesort([1,5,5,2,6,6,9,3]))
