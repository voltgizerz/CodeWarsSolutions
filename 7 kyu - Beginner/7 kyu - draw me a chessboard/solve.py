def chess_board(rows, columns):
    list = []
    for i in range(rows):
        temp =[]
        xo = ["O","X"]
        if i%2!=0:
            xo[0] = "X"
            xo[1] = "O"
        for x in range(columns):
            if x%2==0:
                temp.append(xo[0])
            else:
                temp.append(xo[1])
        list.append(temp)
    return list