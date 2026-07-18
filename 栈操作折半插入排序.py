def binary_sort(a):
    for i in range(0, len(a)):
        index = a[i]
        low = 0
        hight = i - 1
        while low <= hight:
            mid = (low + hight) // 2
            if index > a[mid]:
                low = mid + 1
            else:
                hight = mid - 1
        for j in range(i, low, -1):
            a[j] = a[j - 1]
        a[low] = index

li=[59,12,77,64,72,69,46,89,31,9]
print('before: ',li)
binary_sort(li)
print('after: ',li)
