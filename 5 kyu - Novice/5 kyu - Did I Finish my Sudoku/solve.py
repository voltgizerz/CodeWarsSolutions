def done_or_not(board): #board[i][j]
   #CHECKING ROWS
    for i in range(9):
        if sum(board[i])!=45: return 'Try again!'
    #CHECKING COLS
    for j in range(9):
        list = []
        for i in range(9):
            for x in range(j,j+1):
                list.append(board[i][x])
        if sum(list)!=45: return 'Try again!'
    #CHECKING 3*3
    for i in range(0, 9, 3):
      for j in range(0, 9, 3):
        list = []
        list.extend(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
        if sum(list)!=45: return 'Try again!'
    return 'Finished!'