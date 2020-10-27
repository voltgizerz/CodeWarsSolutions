def max_sequence(arr):
    if arr!=[]:
        max_now = arr[0]
        max_all = arr[0]
        for i in range(1,len(arr)):
            max_now = max(arr[i],max_now +arr[i])
            if  max_now > max_all:
                max_all=max_now
        return max_all if max_all>0 else 0
    return 0