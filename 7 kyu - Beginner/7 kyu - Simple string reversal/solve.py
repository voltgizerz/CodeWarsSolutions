def solve(s):
    space = [i for i in range(len(s)) if s.startswith(" ", i)]
    s = s[::-1].replace(" ","")
    for i in space:
        s = s[:i]+" "+s[i:]
    return s