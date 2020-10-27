def positive_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i]>0: sum += arr[i] 
    return sum