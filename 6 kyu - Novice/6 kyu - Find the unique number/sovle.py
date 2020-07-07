from collections import Counter
def find_uniq(arr):
    for e,v in Counter(arr).items():
        if v==1:return e