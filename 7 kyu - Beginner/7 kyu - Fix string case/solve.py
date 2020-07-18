def solve(s):
    upper = [x for x in s if x.isupper()]
    lower = [x for x in s if x.islower()]
    return s.upper() if len(upper)>len(lower) else s.lower()