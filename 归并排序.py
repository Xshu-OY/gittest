def merge(left,right):
    i,j=0,0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(alist):
    if len(alist)<=1:
        return alist
    mid = len(alist)//2
    left =merge_sort(alist[:mid])
    right =merge_sort(alist[mid:])
    return merge(left,right)

def main():
    li=[9,4,6,2,1,7]
    print("befroe: ",li)
    print("after: ",merge_sort(li))


if __name__=='__main__':
    main()











