def group_groceries(groceries):
    list = groceries.split(",")
    fruit = sorted([x for x in list if "fruit" in x])
    meat = sorted([x for x in list if "meat" in x])
    vegetable = sorted([x for x in list if "vegetable" in x])
    other = [x for x in list if ("fruit" not in x) and "meat" not in x and "vegetable" not in x ]
    for x in range(len(other)):
        split = other[x].split("_")
        other[x]= split[1]
    other.sort()
    return ("fruit:"+",".join(fruit)).replace("fruit_","")+("\nmeat:"+",".join(meat)).replace("meat_","")+("\nother:"+",".join(other)).replace("other_","")+("\nvegetable:"+",".join(vegetable)).replace("vegetable_","")