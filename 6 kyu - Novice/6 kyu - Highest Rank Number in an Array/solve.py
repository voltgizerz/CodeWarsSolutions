from collections import Counter
def highest_rank(arr):
    m=max(Counter(arr).values())
    list = [k for k in Counter(arr) if Counter(arr).get(k) == m]
    list.sort(reverse=True)
    return list[0]