def sequential_search(lis, item):
    pos=0
    found = False
    while pos < len(lis) and  not found:
        if lis[pos] == item:
            found = True
        else:
            pos = pos+1
    return(found)
if __name__ == '__main__':
    testlist = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = sequential_search(testlist, 5)
    print(result)
    result = sequential_search(testlist, 4)
    print(result)
