def accum(s):
    value = ""
    for i in range(len(s)):
        for z in range(0,i+1):
            if z == 0:
                value += s[i].upper()
            else:
                value += s[i].lower()
        if (i+1!= len(s)): value +="-"
    return value