def stray(arr):
    arrset= list(set(arr))
    for i in arrset:
        if arr.count(i)==1:
            return i
        else:
            return arrset[1]