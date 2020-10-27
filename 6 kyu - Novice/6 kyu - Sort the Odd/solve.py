def sort_array(source_array):
    odd = [i for i in source_array if i%2 == 1]
    odd.sort()
    cnt =0
    for x in range(len(source_array)):
        if source_array[x]%2 == 1:
           source_array[x]=odd[cnt]
           cnt+=1
    return source_array