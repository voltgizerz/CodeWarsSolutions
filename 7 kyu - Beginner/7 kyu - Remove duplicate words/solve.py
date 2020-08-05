def remove_duplicate_words(s):
    x=[]
    for i in s.split(" ") :
        if i not in x:
            x.append(i)
    return " ".join(x)