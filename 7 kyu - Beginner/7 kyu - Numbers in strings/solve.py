def solve(s):
    word =""
    list = []
    for i in s:
        if i.isnumeric():
            word+=i
        else:
            if word!="":
                list.append(word)
            word =""
    if word!="":
        list.append(word)
    return max([int(i) for i in list])