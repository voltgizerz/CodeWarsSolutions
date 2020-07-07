def high(x):
    list = x.split(" ")
    save = 0
    highest = 0
    for i in range(len(list)):
        sum = 0
        for x in range(len(list[i])):
            sum += ord(list[i][x]) - 96
        if save<sum:
            save = sum
            highest =list[i]
    return highest