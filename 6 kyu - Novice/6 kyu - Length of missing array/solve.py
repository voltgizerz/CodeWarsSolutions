def get_length_of_missing_array(array_of_arrays):
    list = []
    if array_of_arrays and (None not in array_of_arrays):
        for i in range(len(array_of_arrays)):
            if array_of_arrays[i]!=None: 
                list.append(len(array_of_arrays[i]))
        list.sort()
        start = list[0]
        for i in range(len(list)):
            if list[i]!=start:
                return start
            elif list[i]==0:
                return 0
            start+=1
    else:
        return 0