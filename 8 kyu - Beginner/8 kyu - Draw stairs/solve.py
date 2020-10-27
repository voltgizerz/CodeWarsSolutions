def draw_stairs(n):
    stairs =""
    space = 0
    for i in range(n):
        if i !=0:stairs +="\n"
        stairs +=(" ")*space+"I"
        space+=1
    return stairs