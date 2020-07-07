def array_diff(a, b):
    ans =[]
    for i in range(len(a)):
        if a[i] not in b: ans.append(a[i])
    return ans