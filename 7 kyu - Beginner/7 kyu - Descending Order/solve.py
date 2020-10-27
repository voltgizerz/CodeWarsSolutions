def descending_order(num):
    list  = [int(x) for x in str(num) ]
    list.sort(reverse=True)
    return int("".join([str(x) for x in list ]))