def binarysearch(a, num):
    length = len(a)
    low = 0     # 最小数下标
    high = length - 1           # 最大数的下标
    while low <= high:
        mid = int(low + ((high - low) / 2))   # 取中间值
        if a[mid] < num:
            low = mid + 1        # 如果中间值比目标值小,则在mid右半边
        elif a[mid] > num:
            high = mid- 1         # 如果中间值比目标值大,则在mid左半边找
        else:
            return mid            #查找到，位置是mid+1
    return -1                    #没查到
if __name__ == '__main__':
    b = [1, 3, 4, 8, 22, 65, 73, 90]
    print(b)
    a = binarysearch(b, 22)
    print(a)
    c = binarysearch(b, 21)
    print(c) 
