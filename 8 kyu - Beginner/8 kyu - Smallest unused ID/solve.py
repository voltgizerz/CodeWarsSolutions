def next_id(arr):
    ans = None
    for a in range(0,len(arr)):
        if a not in arr:
            return a
    return len(arr) if ans == None and len(arr)!=0 else 0