def move_zeros(array):
    zeros =[i for i in array if type(i)!=bool].count(0)
    array = [i for i in array if i != 0 or type(i)==bool]
    for i in range(zeros):
        array.append(0)
    return array