def life_path_number(birthdate):
    birthdate = birthdate.split("-")
    temp = []
    for i in birthdate:
        z = int(i)
        while len(str(z))!=1:
            z = sum([int(x) for x in str(z)])
        else:
            temp.append(z)
            
    res = sum(temp)
    while len(str(res))!=1:
         res = sum([int(x) for x in str(res)])
    return res
        