#【堆排序代码一】
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)
def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr

L = [50, 16, 30, 10, 60,  90,  2, 80, 70] 
print(heapSort(L))

#【堆排序代码二】采用collections库的deque实现，见附录C。

from collections import deque
def swap_param(L, i, j):                   #把堆顶元素和堆末尾的元素交换
    L[i], L[j] = L[j], L[i]
    return L
def heap_adjust(L, start, end):            #heap_ adjust函数用于调整为大根堆
    temp = L[start]
    i = start
    j = 2 * i
    while j <= end:               #代表在调整完整棵树树之前一直进行循环
        if (j < end) and (L[j] < L[j + 1]):   #保证 j 取到较大子树的坐标
            j += 1
        if temp < L[j]:   
 #如果子树的根节点小于子树的值, 就把根节点和较大的子树的值进行交换
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp
def heap_sort(L):                # heap_sort函数用于构造大根堆
    L_length = len(L)- 1       #引入一个辅助空间
    first_sort_count = L_length // 2
    for i in range(first_sort_count):     #把序列调整为一个大根堆
        heap_adjust(L, first_sort_count - i, L_length)
    for i in range(L_length - 1):           
        L = swap_param(L, 1, L_length - i)  
#把堆顶元素和堆末尾的元素交换（引入的一个辅助空间，序列长度减1）
        heap_adjust(L, 1, L_length - i - 1)      #把剩下的元素调整为一个大根堆
    return [L[i] for i in range(1, len(L))]
def main():
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))
if __name__ == '__main__':
    main()




import heapq
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]
if __name__ == '__main__':
    li=[50, 16, 30, 10, 60, 90, 2, 80, 70] 
    print("before: ",li)
    h=heapsort(li)
    print("after: ",h)



