import math
def cakes(recipe, available):
    list = []
    for i,v in recipe.items():
        if available.get(i)!=None:
            list.append(math.floor(available.get(i)/v))
        else:
            return 0
    return min(list)