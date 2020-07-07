def in_array(array1, array2):
    list =[]
    for item in array1:
        for i in array2:
            if item in i and item not in list:
                list.append(item)
    list.sort()
    return list