def clean_string(s):
    w = ""
    for i in s:
        if i!="#":
            w+=i
        else:
            w = w[:len(w)-1]
    return w