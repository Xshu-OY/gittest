def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
arr = [59,12,77,64,72,69,46,89,31,9]
print('before: ',arr)
insertionSort(arr) 
print ("after:") 
for i in range(len(arr)): 
    print ("%d   "%arr[i],end='')
