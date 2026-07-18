def shell_sort(alist):
    n=len(alist)
    gap=n//2    
    while gap>0:
        for i in range(gap,n):
            j=i
            while j>=gap and alist[j-gap]>alist[j]:
                alist[j-gap],alist[j]=alist[j],alist[j-gap]
                j-=gap
        gap =gap//2
li=[11,9,84,32,92,26,58,91,35,27,46,28,75,29,37,12]
print('before: ',li)
shell_sort(li)
print('after: ',li)
