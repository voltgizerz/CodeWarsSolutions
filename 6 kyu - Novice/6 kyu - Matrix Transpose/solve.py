def transpose(matrix):
    ans =[]
    for i in range(len(matrix[0])):
        row =[]
        for x in matrix:
            row.append(x[i])
        ans.append(row)
    return ans