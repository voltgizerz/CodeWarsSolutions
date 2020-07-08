def comp(array1, array2):
    print(array1,array2)
    cmp =[]
    if array2!=None and array1!=None:
        for i in range(len(array1)):
            cmp.append(pow(array1[i],2))
        return sorted(cmp)==sorted(array2)
    else:
        return False