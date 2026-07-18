def selection_sort(alist):
    n=len(alist)
    for i in range(0,n):
        min = i                       #将当前下标定义为最小值下标
        for j in range(i+1,n):
            if alist[j]<alist[min]:                #如果有小于当前最小值的关键字 
                min = j                #将此关键字的下标赋值给min_index 
        if  i != min:   #i 不是最小数时，将i 和最小数交换
            alist[i],alist[min]=alist[min],alist[i]
li=[5,2,1,8,3,4,6,7]
print('before:',li)
selection_sort(li)
print('after:',li)
