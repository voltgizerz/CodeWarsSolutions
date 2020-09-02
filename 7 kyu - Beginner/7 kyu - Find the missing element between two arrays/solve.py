def find_missing(arr1, arr2):
    arr1.sort()
    arr2.sort()
    print(arr1,arr2)
    for i,e in enumerate(arr1):
        if len(arr2)>i:
            if e!= arr2[i]:
                return e
        else:
            return e