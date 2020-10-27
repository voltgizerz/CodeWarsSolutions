import math
def waterbombs(fire, w):
    list = fire.split("Y")
    sum =0
    for i in range(len(list)):
       sum += math.ceil((len(list[i]))/w)
    return sum