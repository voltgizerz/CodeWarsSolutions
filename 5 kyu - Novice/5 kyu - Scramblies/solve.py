from collections import Counter
def scramble(s1, s2):
    dict1 = Counter(s1)
    dict2 = Counter(s2)
    for a,v in dict2.items():
        if dict1.get(a)==None or dict1.get(a)<v:
            return False
    return True