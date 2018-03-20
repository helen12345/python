def quicksort(ls):
    if len(ls) < 2:
        return ls
    else:
        num = ls[0];
        less = [i for i in ls[1:] if i<= num]
        greater = [j for j in ls[1:] if j>num]
        return quicksort(less) + [num] + quicksort(greater)
print(quicksort([1,3,2,2,6,7,9,7]))



