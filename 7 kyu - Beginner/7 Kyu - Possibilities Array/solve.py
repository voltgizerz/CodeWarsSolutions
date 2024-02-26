def is_all_possibilities(arr):
    isPossible = True
    for i in range(0, len(arr)):
        if i not in arr:
            isPossible = False
            
    return isPossible
        
