def uniq(seq): 
    a =[]
    for i in seq:
        if not a:
            a.append(i)
        elif a[-1]!=i:
            a.append(i)
    return a