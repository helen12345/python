#method 1
def insertsort(ls):
    ls_new = [ls[0]]
    for i in range(1,len(ls)):
        temp = 0
        for j in range(len(ls_new)):
            if ls[i]<ls_new[j]:
                ls_new = ls_new[:j]+[ls[i]]+ls_new[j:]
                temp =1
                break
        if temp == 0:
            ls_new.append(ls[i])
    return ls_new
print(insertsort([2,1,4,5,3,7,8,9,4,5,2,1,2]))

#method 2
# 直接插入排序
def insertSort(relist):
    len_ = len(relist)
    for i in range(1, len_):
        for j in range(i):
            if relist[i] < relist[j]:
                relist.insert(j, relist[i])  # 首先碰到第一个比自己大的数字，赶紧刹车，停在那，所以选择insert
                relist.pop(i + 1)  # 因为前面的insert操作，所以后面位数+1，这个位置的数已经insert到前面去了，所以pop弹出
                break
    return relist


print(insertSort([2,1,4,5,3,7,8,9,4,5,2,1,2]))


#method 3
def insertsort(ls):
    for i in range(1,len(ls)):
        for j in range(i):
            if ls[i]<ls[j]:
                ls.insert(j,ls[i])
                ls.pop(i+1)
    return ls
print(insertSort([2,1,4,5,3,7,8,9,4,5,2,1,2]))











