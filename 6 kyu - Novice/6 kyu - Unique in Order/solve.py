def unique_in_order(iterable):
    list =[]
    for i in range(len(iterable)):
        if i == 0 or list[-1]!=iterable[i]:
            list.append(iterable[i])
    return list