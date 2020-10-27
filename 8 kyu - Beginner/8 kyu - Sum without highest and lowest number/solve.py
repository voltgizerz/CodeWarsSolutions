def sum_array(arr):
    if arr==None or arr==[] or len(arr)<3:
        return 0
    arr.remove(min(arr))
    arr.remove(max(arr))
    return sum(arr)