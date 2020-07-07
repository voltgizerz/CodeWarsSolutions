def logical_calc(array, op):
    con = ""
    if op =="XOR":
        for i in range(len(array)):
            con += str(array[i])
            if i+1 != len(array): con +=" ^ "
        return eval(con) 
    else:
        for i in range(len(array)):
            con += str(array[i])
            if i+1 != len(array): con +=" "+op.lower()+" "
        return eval(con) 