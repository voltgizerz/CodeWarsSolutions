import math
def data_reverse(data):
    data = [data[8*i:8*i+8] for i in range(0,math.ceil(len(data)/8))]
    data.reverse()
    list = []
    for i in data:
        list.extend(i)
    return list