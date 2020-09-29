def dup(arry):
    a = []
    for x in arry:
        w = ""
        for e in x:
            if w=="":
                w+=e
            elif w[-1]!=e:
                w+=e
        a.append(w)
    return a