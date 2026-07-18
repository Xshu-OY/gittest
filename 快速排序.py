def quick_sort(alist ,start,end):
    if start>=end:
        return
    mid =alist[start]
    low=start
    high =end
    while low < high:
        while low<high and alist[high]>=mid:
            high -=1
        alist[low]=alist[high]
        while low<high and alist[low]<mid:
            low +=1
        alist[high]=alist[low]
        alist[low]=mid
    quick_sort(alist ,start,low-1)
    quick_sort(alist ,low+1,end)

li=[48,36,61,99,81,14,30]
print('before:',li)
quick_sort(li,0,len(li)-1)
print('after:',li)
