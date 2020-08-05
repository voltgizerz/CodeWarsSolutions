from collections import Counter
def no_repeat(string):
    for a,v in Counter(string).items():
        if v==1: return a