def parts_sums(ls):
    list =[sum(ls)]
    for i in ls:
        list.append(list[-1]-i)
    return list