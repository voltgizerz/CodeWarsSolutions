from collections import Counter
def string_letter_count(s):
    list = Counter(s.lower())
    all = []
    for i,j in list.items():
        if i.isalpha():
            all.append(str(j)+i)
    all.sort(key = lambda x:x[-1])
    return "".join(all)