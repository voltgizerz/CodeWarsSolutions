def capitalize(s):
    save = ""
    list = []
    for i in range(len(s)):
        if i%2==0:
            save += s[i].upper()
        else:
            save += s[i].lower()
    list.append(save)
    list.append(save.swapcase())
    return list