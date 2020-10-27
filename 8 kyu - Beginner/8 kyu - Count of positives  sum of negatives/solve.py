def count_positives_sum_negatives(arr):
    sum = 0
    cnt = 0
    if not arr: return []
    for i in arr:
        if i<=0:
            sum+=i
        else:
            cnt+=1
    return [cnt,sum]