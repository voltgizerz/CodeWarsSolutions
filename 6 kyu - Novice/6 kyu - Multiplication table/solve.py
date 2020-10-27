def multiplication_table(size):
    list = []
    cnt=1
    for i in range(size):
        a =[]
        x = 0
        for z in range(size):
            x+=cnt
            a.append(x)
        list.append(a)
        cnt+=1
    return list