def even_odd(arr):
    guess =1
    for i in range(len(arr)):
        if i%2==1 or i==0:
            guess*=arr[i]
        else:
            guess+=arr[i]
    return guess