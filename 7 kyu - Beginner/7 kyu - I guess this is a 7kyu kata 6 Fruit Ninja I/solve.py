import math
def cut_fruits(fruits):
    cut_fruits = []
    for i in fruits:
        if i in FRUIT_NAMES:
            cut_fruits.extend([i[0:math.ceil(len(i)/2)],i[math.ceil(len(i)/2):]])
        else:
            cut_fruits.append(i)
    return cut_fruits