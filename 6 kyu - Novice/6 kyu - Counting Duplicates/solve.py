from collections import Counter
def duplicate_count(text):
    list = Counter(text.lower())
    cnt = 0
    for a,v in list.items():
        if v>1: cnt +=1
    return cnt